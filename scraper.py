page.goto("https://www.facebook.com/ChimbotenoticiasOficial")

page.wait_for_timeout(5000)

print(page.title())

print(page.url)

print(page.content())
