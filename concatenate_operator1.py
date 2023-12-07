from PIL import Image
import numpy as np

# Memuat gambar menggunakan Pillow
amg_pillow = Image.open('citra.jpg').convert('L')

# Mengekstrak wilayah yang diminati
bmg_pillow = amg_pillow.crop((387, 102, 544, 317))

# Membuat gambar baru dengan ukuran yang sama seperti gambar asli
cmg_pillow = Image.new('L', (640, 585), color=255)

# Menyisipkan wilayah yang diekstrak ke dalam gambar baru
cmg_pillow.paste(bmg_pillow, (0, 0))

# Mengonversi hasil ke dalam array NumPy jika diperlukan
cmg_pillow_array = np.array(cmg_pillow)

# Jika ingin menyimpan hasil
cmg_pillow.save('open_image/output.png')
cmg_pillow.show()

