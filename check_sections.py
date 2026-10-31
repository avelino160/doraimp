import re

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Let's inspect all <section> elements
sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\'][^>]*>', html)
print('Sections found:', sections)
