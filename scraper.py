from playwright.sync_api import sync_playwright

print("Iniciando...")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(
        "https://facebook.com",
        wait_until="networkidle",
        timeout=60000
    )

    print(page.title())
    print(page.url)

    browser.close()

print("Finalizado")
