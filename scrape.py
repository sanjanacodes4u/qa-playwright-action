from playwright.sync_api import sync_playwright
import re

seeds = list(range(52, 62))  # 52 to 61

total_sum = 0

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    for seed in seeds:
        url = f"https://sanand0.github.io/tdsdata/seed_{seed}.html"
        page.goto(url)

        content = page.content()
        numbers = re.findall(r"\d+", content)

        total_sum += sum(map(int, numbers))

    browser.close()

print("FINAL TOTAL:", total_sum)
