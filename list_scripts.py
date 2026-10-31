import re

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

scripts = re.findall(r'<script[^>]*src=["\']([^"\']+)["\'][^>]*>', html)
print('External scripts in index.html:', scripts)
