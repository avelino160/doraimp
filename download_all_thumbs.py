import urllib.request
import os

# Todos os video IDs do dorama-links.js
video_ids = [
    'VLTvfq8IrLo','ZyfWKGuH7GY','RPn1a_FAWMQ','UEkkVyFBdBc','09iQYTcZfsg',
    'nsHJX5QGhYc','XtzPQ-VXqPk','emywT4z7Eps','5YQbwGcAm-M','9XfWAkwN4Ms',
    '7BYqD6rhlw0','t3Kd5-vI6zc','SanSc_fZlgA','z06aaEgKnyk','tnbIP95rYPM',
    '1O73X_1HAG8','IEnw0cHqeJQ','KiZVO_nLLDg','2Qjazbyy6F0','E519D8qHTnE',
    'NZ8BMz6yIis','GH1y7hsZDV4','CR7tQD2w2vk','KBFARvbxTNA','dCqEq8tzFJo',
    '1JFLVEs8izM','T9ye-RPMWQI','pMhil8m_CzU','FUE_6Ls--TI','pBfEXXTZh7c',
    'jf-Nsn14aLc','B3Tv0dm3HAs','X-4r0X4vjBk','67K5SK2hHLg','nubU-5C71zI',
    # Novos
    'gEacqyHO1D4','NRVCpQ8sxeA','0ycWcvAEe5M','VeGy8mK-_MU','D_RCAL23TVg',
    'FLCqxrB3rOU','izfqPk08Vkk','l6A_2fVMJPQ','J3DfQn1K6rg','awkcQu7OVZ8',
    'ym1e67vyBbQ','9Y1ztjlbXUk','aoAOkaLofAI','q2Ybp21Eing','MnY3mzZeyv8',
    'qROR2BTupVE','FubJEZkBIew','u3jmEqIoY3A','Ty5EdzgvcUA','xDxGu3anP_M',
    '68G7-C9hMTI','a79hDl9mbwM','1LPlcimJIdE','8_gzc3gmQC0','XGWScFNq6uc',
    'dJKN--qTdVA','AX2lAdnRwgM','6SW6mTUtA3w','QoHgX6xdo_g','Th4dBDxutfE'
]

pics_dir = os.path.join(os.path.dirname(__file__), 'pics')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'
}

ok = 0
fail = 0

for vid_id in video_ids:
    out_path = os.path.join(pics_dir, f'yt_{vid_id}.jpg')
    if os.path.exists(out_path) and os.path.getsize(out_path) > 5000:
        print(f'OK (cached): {vid_id}')
        ok += 1
        continue

    downloaded = False
    for quality in ['maxresdefault', 'hqdefault', 'mqdefault', 'sddefault']:
        url = f'https://i.ytimg.com/vi/{vid_id}/{quality}.jpg'
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = resp.read()
            if len(data) > 5000:
                with open(out_path, 'wb') as f:
                    f.write(data)
                print(f'OK ({quality}): {vid_id} - {len(data)} bytes')
                ok += 1
                downloaded = True
                break
        except Exception as e:
            continue

    if not downloaded:
        print(f'FALHOU: {vid_id}')
        fail += 1

print(f'\nTotal: OK={ok} | Falhou={fail}')
