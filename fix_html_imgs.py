import re
import os

# IDs com thumbnails locais válidas (> 5KB)
VALID_IDS = {
    '0ycWcvAEe5M','1LPlcimJIdE','67K5SK2hHLg','68G7-C9hMTI','6SW6mTUtA3w',
    '8_gzc3gmQC0','9Y1ztjlbXUk','a79hDl9mbwM','aoAOkaLofAI','awkcQu7OVZ8',
    'AX2lAdnRwgM','dJKN--qTdVA','D_RCAL23TVg','E519D8qHTnE','FLCqxrB3rOU',
    'FubJEZkBIew','gEacqyHO1D4','GH1y7hsZDV4','izfqPk08Vkk','J3DfQn1K6rg',
    'KBFARvbxTNA','l6A_2fVMJPQ','MnY3mzZeyv8','NRVCpQ8sxeA','nubU-5C71zI',
    'q2Ybp21Eing','QoHgX6xdo_g','qROR2BTupVE','T9ye-RPMWQI','Th4dBDxutfE',
    'Ty5EdzgvcUA','u3jmEqIoY3A','VeGy8mK-_MU','VLTvfq8IrLo','X-4r0X4vjBk',
    'xDxGu3anP_M','XGWScFNq6uc','ym1e67vyBbQ'
}

# Fallback: usar uma imagem genérica disponível para IDs inválidos
FALLBACK_LOCAL = 'pics/yt_VLTvfq8IrLo.jpg'

base = r"c:\Users\Aveli\Downloads\web2.zip_dorama_list_creation_vercel_app"
html_path = os.path.join(base, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

original = html

def replace_img_src(m):
    vid_id = m.group(1)
    rest = m.group(2)  # alt="..." class="..."
    
    if vid_id in VALID_IDS:
        local_src = f'pics/yt_{vid_id}.jpg'
        # Usar imagem local sem onerror necessário
        return f'src="{local_src}"{rest}'
    else:
        # Imagem não disponível: usar fallback local
        return f'src="{FALLBACK_LOCAL}"{rest}'

# Padrão: src="https://img.youtube.com/vi/{ID}/hqdefault.jpg"
pattern = r'src="https://img\.youtube\.com/vi/([^/]+)/hqdefault\.jpg"((?:\s+[^>]*?)*)'

new_html = re.sub(pattern, replace_img_src, html)

changes = html.count('img.youtube.com') 
replaced = new_html.count('img.youtube.com')
print(f"Imagens remotas antes: {changes}")
print(f"Imagens remotas após: {replaced}")
print(f"Substituídas: {changes - replaced}")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("HTML atualizado!")
