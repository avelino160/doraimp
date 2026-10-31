import re

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Let's search for "Mais populares" and "populares"
pop_m = re.search(r'<section[^>]*id=[^>]*populares[^>]*>(.*?)(?=<section|<footer>|$)', html, re.DOTALL)
if pop_m:
    print('Found #populares section!')
    cards = re.findall(r'<button class="group relative w-full[^"]*"[^>]*>(.*?)</button>', pop_m.group(0), re.DOTALL)
    print(f'Total cards in #populares: {len(cards)}')
