from playwright.sync_api import sync_playwright
import re
import json

URL = "https://www.facebook.com/ChimbotenoticiasOficial"

print("Iniciando scraper...")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(URL, wait_until="networkidle", timeout=60000)
    page.wait_for_timeout(5000)

    html = page.content()

    print("Buscando JSON interno...")

    # Facebook guarda datos en este patrón
    match = re.search(r"bigPipe\.onPageletArrive\((.*?)\);", html)

    if match:
        print("Datos encontrados")
        try:
            data = json.loads(match.group(1))
            print(json.dumps(data, indent=2)[:2000])
        except Exception as e:
            print("Error parseando JSON:", e)
    else:
        print("No se encontró BigPipe data")

    browser.close()

print("Finalizado")
