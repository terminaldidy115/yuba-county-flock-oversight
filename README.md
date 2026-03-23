# Yuba County Flock Safety ALPR Oversight

Public records research and data pipeline for monitoring the Yuba County Sheriff's Office
deployment of Flock Safety Automatic License Plate Reader (ALPR) cameras, funded by Measure K.

## Contents

- `flock_update.py` — Daily scraper that downloads search audit logs from the Flock Safety
  Transparency Portal, deduplicates records, detects backdated entries, and updates the master Excel file.
- `Master Audit.xlsx` — Raw deduplicated audit log archive.
- `Reports/flock_run_log.csv` — Cumulative log of each daily scrape run.

## Data Source

Flock Safety Transparency Portal: https://transparency.flocksafety.com/yuba-county-ca-so

## Legal Basis

Data collected under California Public Records Act (CPRA) and monitored for compliance
with California Vehicle Code § 2413 (SB 34), which requires ALPR operators to maintain
documented audit logs attributing each search to an authorized user and specific purpose.
