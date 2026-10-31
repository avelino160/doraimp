import re
import os

base = r"c:\Users\Aveli\Downloads\web2.zip_dorama_list_creation_vercel_app"
html_path = os.path.join(base, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# IDs com thumbnails locais válidas
VALID_IDS = [
    '0ycWcvAEe5M','1LPlcimJIdE','67K5SK2hHLg','68G7-C9hMTI','6SW6mTUtA3w',
    '8_gzc3gmQC0','9Y1ztjlbXUk','a79hDl9mbwM','aoAOkaLofAI','awkcQu7OVZ8',
    'AX2lAdnRwgM','dJKN--qTdVA','D_RCAL23TVg','E519D8qHTnE','FLCqxrB3rOU',
    'FubJEZkBIew','gEacqyHO1D4','GH1y7hsZDV4','izfqPk08Vkk','J3DfQn1K6rg',
    'KBFARvbxTNA','l6A_2fVMJPQ','MnY3mzZeyv8','NRVCpQ8sxeA','nubU-5C71zI',
    'q2Ybp21Eing','QoHgX6xdo_g','qROR2BTupVE','T9ye-RPMWQI','Th4dBDxutfE',
    'Ty5EdzgvcUA','u3jmEqIoY3A','VeGy8mK-_MU','VLTvfq8IrLo','X-4r0X4vjBk',
    'xDxGu3anP_M','XGWScFNq6uc','ym1e67vyBbQ'
]

# Remover TODOS os preloads antigos de hqdefault_*.jpg
# <link rel="preload" as="image" href="pics/hqdefault*.jpg" crossorigin="">
old_preload_pattern = r'<link rel="preload" as="image" href="pics/hqdefault[^"]*\.jpg"[^>]*>'
removed = len(re.findall(old_preload_pattern, html))
html = re.sub(old_preload_pattern, '', html)
print(f"Preloads antigos removidos: {removed}")

# Inserir novos preloads para os primeiros 10 IDs válidos (mais relevantes para performance)
priority_ids = VALID_IDS[:10]
new_preloads = ''.join([
    f'<link rel="preload" as="image" href="pics/yt_{vid_id}.jpg" crossorigin="">'
    for vid_id in priority_ids
])

# Inserir antes do </head>
html = html.replace('</head>', new_preloads + '</head>', 1)
print(f"Novos preloads adicionados: {len(priority_ids)}")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Preloads atualizados!")
