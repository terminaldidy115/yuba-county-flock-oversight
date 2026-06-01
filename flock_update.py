"""
Flock Audit Updater - Playwright Version with Run Report
---------------------------------------------------------
Automates clicking "Download CSV" on the Flock transparency page,
merges new rows into Master Audit.xlsx, and saves a run report CSV.

Usage:
    python3 flock_update.py

Requirements:
    pip3 install playwright pandas openpyxl
    python3 -m playwright install chromium
"""

import shutil
import tempfile
import traceback
import pandas as pd
from pathlib import Path
from datetime import datetime
from playwright.sync_api import sync_playwright
from flock_email_reporter import send_flock_report

# ── CONFIG ────────────────────────────────────────────────────────────────────
FLOCK_URL    = "https://transparency.flocksafety.com/yuba-county-ca-so"
MASTER_PATH  = Path("/Users/thomashammock/Desktop/Flock/Master Audit.xlsx")
SHEET_NAME   = "Sheet1"
ID_COLUMN    = "id"
DATE_COLUMN  = "searchDate"
REASON_COL   = "reason"
REPORTS_DIR  = Path("/Users/thomashammock/Desktop/Flock/Reports")
RUN_LOG_PATH = REPORTS_DIR / "flock_run_log.csv"
# ─────────────────────────────────────────────────────────────────────────────


def backup_master(path: Path) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = path.with_name(f"Master Audit BACKUP {timestamp}.xlsx")
    shutil.copy2(path, backup)
    return backup


def download_csv() -> pd.DataFrame:
    with tempfile.TemporaryDirectory() as tmp_dir:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(accept_downloads=True)
            page = context.new_page()

            print(f"  Opening {FLOCK_URL} ...")
            page.goto(FLOCK_URL, wait_until="domcontentloaded", timeout=60000)

            print("  Waiting for page to fully load...")
            page.wait_for_timeout(8000)

            print("  Looking for Download CSV button...")
            btn = page.wait_for_selector(
                "button:has-text('Download CSV'), a:has-text('Download CSV'), "
                "button:has-text('Export'), a:has-text('Export'), "
                "[class*='download'], [class*='export']",
                timeout=30000
            )
            print(f"  Found button: '{btn.inner_text().strip()}'")

            with page.expect_download(timeout=30000) as dl_info:
                btn.click()

            download = dl_info.value
            save_path = Path(tmp_dir) / "flock_export.csv"
            download.save_as(save_path)
            browser.close()

        df = pd.read_csv(save_path, dtype={ID_COLUMN: str})
        return df


def load_master() -> pd.DataFrame:
    if not MASTER_PATH.exists():
        return pd.DataFrame()
    return pd.read_excel(MASTER_PATH, sheet_name=SHEET_NAME, dtype={ID_COLUMN: str})


def merge(master: pd.DataFrame, new_data: pd.DataFrame) -> tuple[pd.DataFrame, int, pd.DataFrame]:
    if master.empty:
        return new_data, len(new_data), new_data

    existing_ids = set(master[ID_COLUMN].dropna())
    new_rows = new_data[~new_data[ID_COLUMN].isin(existing_ids)].copy()
    combined = pd.concat([master, new_rows], ignore_index=True)
    return combined, len(new_rows), new_rows


def find_backdated(master_before: pd.DataFrame, new_rows: pd.DataFrame) -> pd.DataFrame:
    """Find new rows whose searchDate is older than the most recent date already in master."""
    if master_before.empty or new_rows.empty:
        return pd.DataFrame()

    master_before = master_before.copy()
    new_rows = new_rows.copy()
    master_before[DATE_COLUMN] = pd.to_datetime(master_before[DATE_COLUMN], errors="coerce", utc=True)
    new_rows[DATE_COLUMN] = pd.to_datetime(new_rows[DATE_COLUMN], errors="coerce", utc=True)

    most_recent_existing = master_before[DATE_COLUMN].max()
    backdated = new_rows[new_rows[DATE_COLUMN] < most_recent_existing].copy()
    return backdated


def save_run_log(
    run_time: datetime,
    new_rows: pd.DataFrame,
    backdated: pd.DataFrame,
    total_before: int,
    total_after: int,
):
    """Append a single summary row to the running CSV log."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    blank_reason_new = new_rows[
        new_rows[REASON_COL].isna() | (new_rows[REASON_COL].str.strip() == "")
    ] if not new_rows.empty else pd.DataFrame()

    blank_pct = (len(blank_reason_new) / len(new_rows) * 100) if len(new_rows) > 0 else 0

    if not new_rows.empty and DATE_COLUMN in new_rows.columns:
        new_rows_dated = new_rows.copy()
        new_rows_dated[DATE_COLUMN] = pd.to_datetime(new_rows_dated[DATE_COLUMN], errors="coerce", utc=True)
        date_min = new_rows_dated[DATE_COLUMN].min().strftime("%Y-%m-%d")
        date_max = new_rows_dated[DATE_COLUMN].max().strftime("%Y-%m-%d")
    else:
        date_min = ""
        date_max = ""

    # Build backdated detail string (semicolon separated for CSV safety)
    if not backdated.empty:
        backdated_copy = backdated.copy()
        backdated_copy[DATE_COLUMN] = pd.to_datetime(backdated_copy[DATE_COLUMN], errors="coerce", utc=True)
        details = "; ".join(
            f"{row[DATE_COLUMN].strftime('%Y-%m-%d %H:%M UTC')} | reason: {row.get(REASON_COL, '') or '(blank)'}"
            for _, row in backdated_copy.iterrows()
        )
    else:
        details = ""

    new_record = pd.DataFrame([{
        "run_datetime":             run_time.strftime("%Y-%m-%d %H:%M:%S"),
        "master_rows_before":       total_before,
        "master_rows_after":        total_after,
        "new_rows_added":           len(new_rows),
        "new_rows_date_min":        date_min,
        "new_rows_date_max":        date_max,
        "new_rows_blank_reason":    len(blank_reason_new),
        "new_rows_blank_reason_pct": round(blank_pct, 1),
        "backdated_entries":        len(backdated),
        "backdated_detail":         details,
    }])

    if RUN_LOG_PATH.exists():
        existing = pd.read_csv(RUN_LOG_PATH, dtype=str)
        updated = pd.concat([existing, new_record], ignore_index=True)
    else:
        updated = new_record

    updated.to_csv(RUN_LOG_PATH, index=False)
    return RUN_LOG_PATH


def save_master(df: pd.DataFrame):
    MASTER_PATH.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(MASTER_PATH, engine="openpyxl", mode="w") as writer:
        df.to_excel(writer, sheet_name=SHEET_NAME, index=False)


def main():
    run_time = datetime.now()
    print(f"\n[{run_time:%Y-%m-%d %H:%M:%S}] Starting Flock Audit update...")

    if MASTER_PATH.exists():
        backup = backup_master(MASTER_PATH)
        print(f"  Backup saved → {backup.name}")

    print("  Downloading CSV via browser automation...")
    new_data = download_csv()
    print(f"  Downloaded {len(new_data):,} rows from portal")

    master = load_master()
    total_before = len(master)
    print(f"  Master currently has {total_before:,} rows")

    combined, added, new_rows = merge(master, new_data)
    print(f"  New rows added: {added:,}")

    backdated = find_backdated(master, new_rows)
    if len(backdated) > 0:
        print(f"  ⚠️  Backdated entries detected: {len(backdated):,}")
    else:
        print(f"  No backdated entries detected")

    save_master(combined)
    print(f"  Master updated → {MASTER_PATH}")
    print(f"  Total rows now: {len(combined):,}")

    log_path = save_run_log(run_time, new_rows, backdated, total_before, len(combined))
    print(f"  Run log updated → {log_path}")
    print("Done.\n")


if __name__ == "__main__":
    try:
        main()
        send_flock_report(success=True)
    except Exception:
        send_flock_report(success=False, error_details=traceback.format_exc())
        raise
