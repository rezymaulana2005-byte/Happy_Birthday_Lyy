# Script praktis untuk optimasi otomatis thumbnail photobox
import os, glob
from PIL import Image

def main():
    os.makedirs('thumbs', exist_ok=True)
    photos = glob.glob('foto*.jpg') + glob.glob('foto*.jpeg') + glob.glob('foto*.png') + glob.glob('foto*.webp')
    print(f'Ditemukan {len(photos)} file foto untuk dioptimasi...')
    count = 0
    for p in photos:
        digits = ''.join(c for c in os.path.splitext(os.path.basename(p))[0] if c.isdigit())
        if not digits: continue
        num = int(digits)
        dst = f'thumbs/thumb{num}.jpg'
        try:
            im = Image.open(p)
            if im.mode != 'RGB': im = im.convert('RGB')
            w, h = im.size
            new_w = min(w, 440)
            new_h = int(h * (new_w / w))
            im_resized = im.resize((new_w, new_h), Image.Resampling.LANCZOS)
            im_resized.save(dst, 'JPEG', quality=88, optimize=True)
            count += 1
        except Exception as e:
            print(f'Gagal {p}: {e}')
    print(f'Selesai! {count} thumbnail siap di folder thumbs/.')

if __name__ == '__main__':
    main()
