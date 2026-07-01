from playwright.sync_api import sync_playwright

URL = "https://www.facebook.com/ChimbotenoticiasOficial"

print("Iniciando scraper...")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(URL, wait_until="domcontentloaded", timeout=60000)

    print("Título:", page.title())
    print("URL:", page.url)

    page.wait_for_timeout(5000)

    content = page.content()
    print("HTML cargado (primeros 500 caracteres):")
    print(content[:500])

    browser.close()

print("Finalizado")
