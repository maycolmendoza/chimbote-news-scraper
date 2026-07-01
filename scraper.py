from playwright.sync_api import sync_playwright

URL = "https://www.facebook.com/ChimbotenoticiasOficial"
BLOCK_WORDS = [
    "sorteo",
    "publicidad",
    "patrocinado",
    "anuncio",
    "whatsapp",
    "compra",
    "oferta",
    "promoción",
    "click aquí",
    "link en bio"
]

print("Iniciando scraper...")

def is_valid_post(text: str) -> bool:
    t = text.lower()
    return not any(word in t for word in BLOCK_WORDS)

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
    
            # FILTRO 1: eliminar vacíos
            if len(text) < 80:
                continue
    
            # FILTRO 2: eliminar basura tipo iconos
            if text.count("\n") < 2:
                continue
    
            # FILTRO 3: debe tener contenido humano
            if "Like" not in text and "Comment" not in text:
                continue
    
            post_id = hashlib.md5(text.encode("utf-8")).hexdigest()
    
            img = post.query_selector("img")
            img_url = img.get_attribute("src") if img else ""
    
            print("\n--- POST VALIDO ---")
            print("ID:", post_id)
            print("IMAGEN:", img_url)
            print(text[:300])
    
        except Exception as e:
            continue
    

 

    browser.close()

print("Finalizado")
