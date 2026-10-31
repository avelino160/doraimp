import re

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

cat_m = re.search(r'<section[^>]*id=[^>]*catalogo[^>]*>(.*?)(?=<section|<footer>|$)', text, re.DOTALL)
if cat_m:
    # Find all cards in catalogo
    cards = re.findall(r'<button class="group relative w-full[^"]*"[^>]*>(.*?)</button>', cat_m.group(0), re.DOTALL)
    print(f"Total cards found in catalogo: {len(cards)}")
    for i, c in enumerate(cards[:5]):
        t = re.search(r'<h3[^>]*>([^<]+)</h3>', c)
        p = re.search(r'<p[^>]*>([^<]+)</p>', c)
        print(f"{i+1}: {t.group(1) if t else 'No title'} | {p.group(1) if p else 'No genre'}")
