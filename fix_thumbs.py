import urllib.request
import os

# IDs com arquivos corrompidos (1.1 KB = placeholder do YouTube)
video_ids_bad = [
    'ZyfWKGuH7GY','RPn1a_FAWMQ','UEkkVyFBdBc','09iQYTcZfsg',
    'nsHJX5QGhYc','XtzPQ-VXqPk','emywT4z7Eps','5YQbwGcAm-M','9XfWAkwN4Ms',
    '7BYqD6rhlw0','t3Kd5-vI6zc','SanSc_fZlgA','z06aaEgKnyk','tnbIP95rYPM',
    '1O73X_1HAG8','IEnw0cHqeJQ','KiZVO_nLLDg','2Qjazbyy6F0',
    'NZ8BMz6yIis','CR7tQD2w2vk','dCqEq8tzFJo',
    '1JFLVEs8izM','pMhil8m_CzU','FUE_6Ls--TI','pBfEXXTZh7c',
    'jf-Nsn14aLc','B3Tv0dm3HAs','pBfEXXTZh7c'
]

pics_dir = os.path.join(os.path.dirname(__file__), 'pics')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Referer': 'https://www.youtube.com/',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
}

ok = 0
fail = 0

for vid_id in set(video_ids_bad):
    out_path = os.path.join(pics_dir, f'yt_{vid_id}.jpg')
    
    downloaded = False
    for quality in ['maxresdefault', 'sddefault', 'hqdefault', 'mqdefault', 'default']:
        url = f'https://i.ytimg.com/vi/{vid_id}/{quality}.jpg'
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = resp.read()
            if len(data) > 10000:  # threshold maior para evitar placeholders
                with open(out_path, 'wb') as f:
                    f.write(data)
                print(f'OK ({quality}): {vid_id} - {len(data)} bytes')
                ok += 1
                downloaded = True
                break
            else:
                print(f'  Placeholder ({quality}): {vid_id} - {len(data)} bytes, tentando outra...')
        except Exception as e:
            print(f'  Erro ({quality}): {vid_id} - {e}')
            continue

    if not downloaded:
        print(f'FALHOU TOTAL: {vid_id}')
        fail += 1

print(f'\nTotal: OK={ok} | Falhou={fail}')
