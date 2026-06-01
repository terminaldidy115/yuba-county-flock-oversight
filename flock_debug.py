"""
Flock Debug Script
Run this to find the exact button text and HTML on the page.
"""
from playwright.sync_api import sync_playwright

FLOCK_URL = "https://transparency.flocksafety.com/yuba-county-ca-so"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    print("Loading page...")
    page.goto(FLOCK_URL, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(5000)

    print("\n--- All buttons on page ---")
    buttons = page.query_selector_all("button")
    for btn in buttons:
        print(f"  button: '{btn.inner_text().strip()}'")

    print("\n--- All links on page ---")
    links = page.query_selector_all("a")
    for link in links:
        txt = link.inner_text().strip()
        href = link.get_attribute("href") or ""
        if txt:
            print(f"  a: '{txt}' href='{href[:80]}'")

    print("\n--- Any element containing 'csv' or 'download' or 'export' ---")
    for tag in ["button", "a", "div", "span"]:
        els = page.query_selector_all(tag)
        for el in els:
            txt = el.inner_text().strip().lower()
            if any(word in txt for word in ["csv", "download", "export"]):
                print(f"  <{tag}>: '{el.inner_text().strip()[:100]}'")

    browser.close()
    print("\nDone.")
