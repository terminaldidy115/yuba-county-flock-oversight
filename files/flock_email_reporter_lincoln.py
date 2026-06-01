"""
flock_email_reporter_lincoln.py
-----------------------
Sends a formatted Flock automation report through macOS Mail.app via AppleScript.
Shows a clean summary of the latest run, a 7-day history table, backdated entry
details, and any flags worth attention.
"""

import subprocess
import csv
import os
import traceback
from datetime import datetime, timedelta

# ─────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────
REPORT_RECIPIENT = "thomas.hammock81@gmail.com"
LOG_PATH         = "/Users/thomashammock/Flock/Reports/flock_run_log_lincoln.csv"
# ─────────────────────────────────────────────


def parse_log(log_path):
    """Parse the CSV and return a list of row dicts, newest first."""
    if not os.path.exists(log_path):
        return []
    with open(log_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return list(reversed(rows))  # newest first


def get_latest_run(rows):
    """Return the most recent row."""
    return rows[0] if rows else {}


def fmt_blank_pct(val):
    """Format blank reason percent cleanly."""
    try:
        f = float(val)
        if f == 0:
            return "0%"
        return f"{f:.1f}%"
    except Exception:
        return "—"


def fmt_int(val):
    try:
        return str(int(float(val))) if val not in ("", None) else "0"
    except Exception:
        return "—"


def build_summary_block(row):
    """Build the clean top-level summary for the latest run."""
    new_rows = fmt_int(row.get("new_rows_added", "0"))
    blank    = fmt_int(row.get("new_rows_blank_reason", "0"))
    blank_pct = fmt_blank_pct(row.get("new_rows_blank_reason_pct", "0"))
    backdated = fmt_int(row.get("backdated_entries", "0"))

    lines = [
        "LATEST RUN SUMMARY",
        "=" * 50,
        f"  Run Time       : {row.get('run_datetime', '—')}",
        f"  Records Before : {fmt_int(row.get('master_rows_before', '—'))}",
        f"  Records After  : {fmt_int(row.get('master_rows_after', '—'))}",
        f"  New Rows Added : {new_rows}",
        f"  Blank Reason   : {blank} ({blank_pct})",
        f"  Backdated      : {backdated}",
    ]
    return "\n".join(lines)


def build_flags(row):
    """Build a flags/warnings section based on the latest run."""
    flags = []
    try:
        if int(float(row.get("new_rows_added", "0"))) == 0:
            flags.append("  ⚠  No new rows added — portal may not have updated yet")
    except Exception:
        pass
    try:
        pct = float(row.get("new_rows_blank_reason_pct", "0"))
        if pct >= 50:
            flags.append(f"  ⚠  High blank reason rate: {pct:.1f}% of new searches undocumented")
    except Exception:
        pass
    try:
        if int(float(row.get("backdated_entries", "0"))) > 0:
            flags.append(f"  ⚠  Backdated entries detected — see detail below")
    except Exception:
        pass

    if not flags:
        return ""

    lines = [
        "",
        "FLAGS",
        "=" * 50,
    ] + flags
    return "\n".join(lines)


def build_history_table(rows):
    """Build a clean 7-day history table without backdated_detail."""
    if not rows:
        return "No runs in the last 7 days."

    headers  = ["Date/Time", "Before", "After", "New", "Blank%", "Back-dated"]
    widths   = [17, 7, 7, 5, 8, 10]

    def fmt_row(vals):
        return "  ".join(str(v).ljust(widths[i]) for i, v in enumerate(vals))

    separator = "-" * (sum(widths) + 2 * len(widths))
    lines = [
        "",
        "7-DAY RUN HISTORY",
        "=" * 50,
        fmt_row(headers),
        separator,
    ]

    for row in rows:
        vals = [
            row.get("run_datetime", "—"),
            fmt_int(row.get("master_rows_before")),
            fmt_int(row.get("master_rows_after")),
            fmt_int(row.get("new_rows_added")),
            fmt_blank_pct(row.get("new_rows_blank_reason_pct")),
            fmt_int(row.get("backdated_entries")),
        ]
        lines.append(fmt_row(vals))

    return "\n".join(lines)


def build_backdated_section(rows):
    """List backdated entry details for any run in the last 7 days that has them."""
    entries = []
    for row in rows:
        try:
            count = int(float(row.get("backdated_entries", "0")))
        except Exception:
            count = 0
        if count > 0:
            detail = row.get("backdated_detail", "").strip()
            entries.append((row.get("run_datetime", "—"), count, detail))

    if not entries:
        return ""

    lines = [
        "",
        "BACKDATED ENTRY DETAIL",
        "=" * 50,
    ]
    for run_time, count, detail in entries:
        lines.append(f"\n  Run: {run_time}  ({count} backdated)")
        lines.append("  " + "-" * 44)
        parts = [p.strip() for p in detail.replace(";", "|").split("|") if p.strip()]
        for part in parts:
            lines.append(f"    {part}")

    return "\n".join(lines)


def build_email_body(success, log_path, error_details=None):
    rows = parse_log(log_path)
    latest = get_latest_run(rows)

    sections = [
        "Lincoln Flock Automation Daily Report",
        f"Status : {'SUCCESS' if success else 'FAILED'}",
        "",
        build_summary_block(latest) if latest else "[No run data found]",
        build_flags(latest) if latest else "",
        build_history_table(rows),
        build_backdated_section(rows),
    ]

    if not success and error_details:
        sections += [
            "",
            "ERROR DETAILS",
            "=" * 50,
            "",
            error_details,
        ]

    return "\n".join(s for s in sections)


def send_via_applescript(subject, body, to_email):
    """Send email through macOS Mail.app via AppleScript."""
    body_escaped = (
        body
        .replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", "\\n")
    )

    script = f"""
tell application "Mail"
    set newMsg to make new outgoing message with properties {{subject:"{subject}", content:"{body_escaped}", visible:false}}
    tell newMsg
        make new to recipient with properties {{address:"{to_email}"}}
    end tell
    send newMsg
end tell
"""
    result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"[Reporter] AppleScript error: {result.stderr.strip()}")
        return False
    print(f"[Reporter] Email sent via Mail.app -> {to_email}")
    return True


def send_flock_report(success: bool, log_path: str = LOG_PATH, error_details: str = None):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    status_label = "SUCCESS" if success else "FAILED"
    subject = f"Lincoln Flock Automation -- {status_label} | {now}"
    body = build_email_body(success, log_path, error_details)
    send_via_applescript(subject, body, REPORT_RECIPIENT)


if __name__ == "__main__":
    print("Sending test report via Mail.app...")
    send_flock_report(success=True, log_path=LOG_PATH)
