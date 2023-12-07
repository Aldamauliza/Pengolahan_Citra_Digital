from PIL import Image
import numpy as np
from scipy.ndimage import shift
import matplotlib.pyplot as plt
# Fungsi pergeseran noninteger
def noninteger_shift(image, shift_amount, order=3):
    return shift(image, shift_amount, order=order)
# Baca gambar asli
fname = 'citra.jpg'
adata = np.array(Image.open(fname).convert('L'))  # Baca dan konversi ke skala abu-abu

# Pergeseran gambar sejauh 10 piksel vertikal dan 25 piksel horizontal (simple shifting)
bdata = shift(adata, (10, 25))

# Pergeseran gambar dengan kontrol nilai piksel yang tidak terdefinisi
cdata = shift(adata, (10, 25), cval=255)

# Pergeseran noninteger gambar sejauh 5.7 piksel vertikal dan 12.3 piksel horizontal
ddata = noninteger_shift(adata, (5.7, 12.3))

plt.figure(figsize=(12, 5))
plt.subplot(141)
plt.imshow(adata, cmap='gray')
plt.title('Original Image')

plt.subplot(142)
plt.imshow(bdata, cmap='gray')
plt.title('Shifted Image')

plt.subplot(143)
plt.imshow(cdata, cmap='gray')
plt.title('Shifted Image with cval=255')

plt.subplot(144)
plt.imshow(ddata, cmap='gray')
plt.title('Noninteger Shifted Image')
plt.show()
