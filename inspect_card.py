import re

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

cat_m = re.search(r'<section[^>]*id=[^>]*catalogo[^>]*>(.*?)(?=<section|<footer>|$)', text, re.DOTALL)
if cat_m:
    first_card = re.search(r'<button class="group relative w-full[^"]*"[^>]*>(.*?)</button>', cat_m.group(0), re.DOTALL)
    if first_card:
        print("FIRST CARD FULL HTML:")
        print(first_card.group(0))
