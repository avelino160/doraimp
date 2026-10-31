import re
import os

base = r"c:\Users\Aveli\Downloads\web2.zip_dorama_list_creation_vercel_app"
html_path = os.path.join(base, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Extrair todos os pares src + h3 title dos cards
# Procurar padrão: src="pics/..." ... <h3 ...>TITULO</h3>
cards = re.findall(r'src="(pics/[^"]+)"[^>]+alt="[^"]*"[^>]*class="h-full[^>]*>.*?<h3[^>]*>([^<]+)</h3>', html, re.DOTALL)

print(f"Cards encontrados: {len(cards)}")
for src, title in cards[:20]:
    print(f"  {src[:40]:42} -> {title[:60]}")
