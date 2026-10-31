import re
import os

base = r"c:\Users\Aveli\Downloads\web2.zip_dorama_list_creation_vercel_app"
html_path = os.path.join(base, 'index.html')

# Mapeamento COMPLETO: título -> video ID correto
# Baseado em dorama-links.js + update-thumbnails.js (que tinha correções)
TITULO_TO_VID = {
    # Da dorama-links.js (IDs corretos)
    'Ela ouviu o namorado ir buscar a ex no aeroporto e decidiu sumir para sempre!': 'gEacqyHO1D4',
    'No dia do casamento, ela pegou o noivo traindo e chamou um bilionário de noivo falso!': 'NRVCpQ8sxeA',
    'Garota pobre faz coração para um carrão. O CEO vê, se apaixona e casa com ela!': '0ycWcvAEe5M',
    'Uma Mecânica Indomável Conquistou o Coração de Um Herdeiro Bilionário': 'VeGy8mK-_MU',
    'Ela salvou uma idosa bilionária! A avó ordenou que seu neto CEO se casasse com ela!': 'D_RCAL23TVg',
    'Escolhe um cadeirante como noivo. Ele é um CEO influente e a rival enlouquece de inveja!': 'FLCqxrB3rOU',
    'CEO atropela uma garota cega e, ao ver seu pingente de jade, reconhece seu grande amor!': 'izfqPk08Vkk',
    'Trocou de noivo na boda! O estranho escolhido era o CEO real e a mima como madame rica!': 'l6A_2fVMJPQ',
    'No primeiro dia como chef, é escolhida pela avó do CEO e acaba se casando com ele!': 'J3DfQn1K6rg',
    'Trocada no altar, ela casou com o homem mais temido para se vingar!': 'awkcQu7OVZ8',
    'Sua Melhor Amiga Matou Sua Mãe e Ela Descobriu que o Próprio Marido Protegia a Assassina!': 'ym1e67vyBbQ',
    'Dispensado pela ex, ele casou de repente com uma CEO linda e poderosa': '9Y1ztjlbXUk',
    'Eles Roubaram Sua Casa e Sua Herança, Mas Ela Voltou com a Prova Definitiva!': 'aoAOkaLofAI',
    'CEO bilionário solteiro há 30 anos evita mulheres, mas se apaixona por estagiária no ônibus': 'q2Ybp21Eing',
    'CEO evitava mulheres até uma empregada que dançava mudar completamente a sua vida!': 'MnY3mzZeyv8',
    'CEO Finge Ser Pobre No Encontro, Todas Fogem! Só Ela Aceita Casar e Ele Se Apaixona!': 'qROR2BTupVE',
    'Seu marido por contrato é seu chefe! Ele manda ficar longe, mas enlouquece de ciúmes!': 'FubJEZkBIew',
    'Família Bilionária Finge Falência Para Testar Noiva, Mas Ela Gasta Tudo Com Eles!': 'u3jmEqIoY3A',
    'Garota Pobre É Forçada A Casar Com Fazendeiro Pela Meia-Irmã! Ele Era O CEO Mais Rico!': 'Ty5EdzgvcUA',
    'Magnata Finge Ser Guarda Pobre Num Encontro. Só A Caipira Gasta Tudo Em Wontons Pra Ele!': 'xDxGu3anP_M',
    'CEO Não Ri Há 20 Anos Até Ver A Noiva Caipira Expulsar A Vilã e Se Apaixona!': '68G7-C9hMTI',
    'Bilionária Se Disfarça De Mendiga Para Testar Os Sogros e Rompe O Noivado!': 'a79hDl9mbwM',
    'Bilionário Volta e Vê A Esposa Vendendo Na Rua, Humilhada Por Parentes!': '1LPlcimJIdE',
    'Ele Achava a Esposa Sem Graça, Até Vê-la Deslumbrante no Dia do Divórcio!': '8_gzc3gmQC0',
    'Meu Companheiro é um Lícano de Rua': 'XGWScFNq6uc',
    'O Acordo Matrimonial do CEO': 'dJKN--qTdVA',
    'Herança e Vingança': 'AX2lAdnRwgM',
    'Após 10 anos amando o vizinho, ela foi desprezada! Um motoqueiro mais jovem a conquistou': '6SW6mTUtA3w',
    'Gênio Médica Não É Alguém Para Mexer': 'QoHgX6xdo_g',
    'Gênio Médica Não É Alguém Para Mexer (Cenas Destacadas)': 'Th4dBDxutfE',
    # Títulos do update-thumbnails.js - mapeamento correto
    'Ele a Procurou por Todo Esse Tempo': '0ycWcvAEe5M',
    'Fuga do Casamento': 'aoAOkaLofAI',
    'Herdeira de Bilhões': 'gEacqyHO1D4',
    'Mimada como uma Rainha': 'izfqPk08Vkk',
    'Um Tapa no CEO': 'q2Ybp21Eing',
    'A Faxineira e o Bilionário': 'VeGy8mK-_MU',
    'Atropelada e Casada num Flash': 'MnY3mzZeyv8',
    'A Mesa Errada': 'qROR2BTupVE',
    'A Mesa Errada (Parte 2)': 'FubJEZkBIew',
    'O CEO Entregador': 'l6A_2fVMJPQ',
    'Vingança Bilionária': 'NRVCpQ8sxeA',
    'Salvo do Fogo': 'u3jmEqIoY3A',
    'A Mãe Escolhida': 'Ty5EdzgvcUA',
    'O CEO que Fingiu ser Cego': 'xDxGu3anP_M',
    'Vingança em Kung-Fu': 'J3DfQn1K6rg',
    'Um Favor de Bilhões': '68G7-C9hMTI',
    'Forçada a Casar com o CEO': 'a79hDl9mbwM',
    'A Enfermeira e o CEO': 'awkcQu7OVZ8',
    'Coach de Amor': '1LPlcimJIdE',
    'Belas Espiãs': '8_gzc3gmQC0',
    'Uma Tigela de Chá': 'ym1e67vyBbQ',
    'Vendida para o Campo': 'XGWScFNq6uc',
    'A Garota do Taco': 'dJKN--qTdVA',
    'Ela Salvou um Bilionário': 'D_RCAL23TVg',
    'A Confeiteira Traída': '9Y1ztjlbXUk',
    'O Casamento Recusado': 'AX2lAdnRwgM',
    'A CEO Disfarçada de Estudante': '6SW6mTUtA3w',
    'A Esposa Ignorada': 'QoHgX6xdo_g',
    'A Irmã e a CEO': 'FLCqxrB3rOU',
    'Humilhada na Empresa': 'a79hDl9mbwM',
    'Casamento pela Mãe': 'J3DfQn1K6rg',
    'O Marido Contratado': 'awkcQu7OVZ8',
    'A Irmã Gêmea': 'FLCqxrB3rOU',
    'O Presidente Mecânico': 'VeGy8mK-_MU',
    'A Filha Perdida': 'nubU-5C71zI',
}

# IDs com arquivo local válido
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

def get_src(vid_id):
    if vid_id in VALID_IDS:
        return f'pics/yt_{vid_id}.jpg'
    return None

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Estratégia: encontrar cada card completo e substituir o src baseado no h3
# Card pattern: <button class="group relative w-full ...">...<img src="...">...<h3>TITULO</h3>...
# Como o HTML é minificado numa linha, precisamos processar segmento a segmento

def fix_card_image(card_html):
    """Dado o HTML de um card, corrige o src da imagem baseado no h3"""
    h3_match = re.search(r'<h3[^>]*>([^<]+)</h3>', card_html)
    if not h3_match:
        return card_html
    
    title = h3_match.group(1).strip()
    vid_id = TITULO_TO_VID.get(title)
    
    if not vid_id:
        print(f"  SEM MAPEAMENTO: {title[:70]}")
        return card_html
    
    new_src = get_src(vid_id)
    if not new_src:
        print(f"  SEM ARQUIVO LOCAL para {vid_id}: {title[:50]}")
        # usar melhor disponivel
        new_src = 'pics/yt_VLTvfq8IrLo.jpg'
    
    # Substituir o src="pics/..." na tag img dentro deste card
    old_src_match = re.search(r'src="(pics/[^"]+)"', card_html)
    if old_src_match:
        old_src = old_src_match.group(1)
        if old_src != new_src:
            print(f"  CORRIGINDO {old_src} -> {new_src} | {title[:50]}")
            card_html = card_html.replace(f'src="{old_src}"', f'src="{new_src}"', 1)
        else:
            print(f"  OK: {new_src} | {title[:50]}")
    
    return card_html

# Encontrar todos os cards (button.group.relative.w-full)
# No HTML minificado, cada card é um <button class="group relative w-full ...">...</button>
card_pattern = r'(<button class="group relative w-full[^>]*>)(.*?)(</button>)'

fixed = 0
errors = 0

def process_card(m):
    global fixed, errors
    full = m.group(0)
    fixed_card = fix_card_image(full)
    if fixed_card != full:
        fixed += 1
    return fixed_card

new_html = re.sub(card_pattern, process_card, html, flags=re.DOTALL)

print(f"\nCards corrigidos: {fixed}")
print(f"Erros: {errors}")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("HTML atualizado com imagens corretas!")
