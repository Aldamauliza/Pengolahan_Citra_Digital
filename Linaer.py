from PIL import Image
import numpy as np
from scipy.ndimage import shift
import matplotlib.pyplot as plt

# Baca gambar asli
fname = 'citra.jpg'
adata = np.array(Image.open(fname).convert('L'))  # Baca dan konversi ke skala abu-abu

# Pergeseran gambar sejauh 10 piksel vertikal dan 25 piksel horizontal
bdata = shift(adata, (10, 25))

# Pergeseran gambar dengan kontrol nilai piksel yang tidak terdefinisi
cdata = shift(adata, (10, 25), cval=255)

# Tampilkan gambar asli, hasil pergeseran, dan hasil pergeseran dengan kontrol nilai piksel tidak terdefinisi
plt.figure(figsize=(10, 5))

plt.subplot(131)
plt.imshow(adata, cmap='gray')
plt.title('Original Image')

plt.subplot(132)
plt.imshow(bdata, cmap='gray')
plt.title('Shifted Image')

plt.subplot(133)
plt.imshow(cdata, cmap='gray')
plt.title('Shifted Image with cval=255')

plt.show()
