with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
html = re.sub(r'placeholder="[^"]*"', 'placeholder="Buscar dorama..."', html)
html = re.sub(r'aria-label="Buscar[^"]*"', 'aria-label="Buscar dorama..."', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Search input attributes cleaned!')
