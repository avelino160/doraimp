with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

if 'filter-catalog.js' not in html:
    # Append before </body>
    html = html.replace('</body>', '<script src="filter-catalog.js"></script></body>')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Added filter-catalog.js to index.html')
else:
    print('filter-catalog.js already in index.html')
