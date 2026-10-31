import urllib.request
import os

video_ids = [
    'RPn1a_FAWMQ','7BYqD6rhlw0','VLTvfq8IrLo','nsHJX5QGhYc','KBFARvbxTNA',
    'X-4r0X4vjBk','UEkkVyFBdBc','9XfWAkwN4Ms','tnbIP95rYPM','KiZVO_nLLDg',
    'NZ8BMz6yIis','dCqEq8tzFJo','ZyfWKGuH7GY','09iQYTcZfsg','XtzPQ-VXqPk',
    'emywT4z7Eps','5YQbwGcAm-M','t3Kd5-vI6zc','SanSc_fZlgA','z06aaEgKnyk',
    '1O73X_1HAG8','IEnw0cHqeJQ','2Qjazbyy6F0','E519D8qHTnE','GH1y7hsZDV4',
    'CR7tQD2w2vk','1JFLVEs8izM','T9ye-RPMWQI','pMhil8m_CzU','Th4dBDxutfE',
    'pBfEXXTZh7c','jf-Nsn14aLc','B3Tv0dm3HAs','67K5SK2hHLg','nubU-5C71zI'
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
    
    # Tentar maxresdefault primeiro, depois hqdefault, depois mqdefault
    downloaded = False
    for quality in ['maxresdefault', 'hqdefault', 'mqdefault', 'sddefault']:
        url = f'https://i.ytimg.com/vi/{vid_id}/{quality}.jpg'
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
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
