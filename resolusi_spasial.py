import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk mengurangi resolusi spasial dengan faktor tertentu
def downsample_image(image, factor):
    return image[::factor, ::factor]

# Load gambar asli
original_image = plt.imread('citra.jpg')  # Ganti dengan nama gambar asli dan pathnya

# Tampilkan gambar asli
plt.figure(figsize=(5, 5))
plt.imshow(original_image, cmap='gray')
plt.title('Gambar Asli (Resolusi 128x128)')
plt.show()

# Pengurangan resolusi spasial
resolutions = [2, 8, 26]  # Faktor penurunan resolusi
for factor in resolutions:
    downsampled_image = downsample_image(original_image, factor)

    # Tampilkan gambar dengan resolusi yang dikurangi
    plt.figure(figsize=(5, 5))
    plt.imshow(downsampled_image, cmap='gray')
    plt.title(f'Gambar dengan Resolusi Spasial {128 // factor}x{128 // factor} (⇓{factor})')
    plt.show()
