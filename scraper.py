from playwright.sync_api import sync_playwright

URL = "https://www.facebook.com/ChimbotenoticiasOficial"

print("Iniciando scraper...")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(URL, wait_until="domcontentloaded", timeout=60000)

    page.wait_for_timeout(8000)

    print("Buscando posts...")

    posts = page.query_selector_all('div[role="article"]')

    print(f"Posts encontrados: {len(posts)}")

    for i, post in enumerate(posts):
    
        try:
            text = post.inner_text().strip()
    
            # filtro básico para eliminar basura
            if len(text) < 50:
                continue
    
            print(f"\n--- POST {i+1} ---")
            print(text[:600])
    
        except:
            continue

    browser.close()

print("Finalizado")
