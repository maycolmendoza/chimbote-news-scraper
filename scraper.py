page.goto("TU PAGINA")

page.wait_for_timeout(5000)

print(page.title())

print(page.url)

print(page.content())
