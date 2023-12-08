import imageio.v2 as imageio
import scipy.ndimage as nd
import matplotlib.pyplot as plt

# Membaca gambar dengan mode='F'
amg = imageio.imread('citra.jpg', mode='F') < 100

# Melakukan binary dilation dengan iterasi yang berbeda
bmg = nd.binary_dilation(amg, iterations=12) ^ nd.binary_dilation(amg, iterations=9)
cmg = nd.binary_dilation(amg, iterations=6) ^ nd.binary_dilation(amg, iterations=3)

# Menggabungkan hasilnya menggunakan operator bitwise OR (`|`)
dmg = amg | bmg | cmg

# Menampilkan gambar awal
plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(amg, cmap='gray')

# Menampilkan hasil dilasi biner pertama
plt.subplot(2, 2, 2)
plt.title('Binary Dilation 1')
plt.imshow(bmg, cmap='gray')

# Menampilkan hasil dilasi biner kedua
plt.subplot(2, 2, 3)
plt.title('Binary Dilation 2')
plt.imshow(cmg, cmap='gray')

# Menampilkan hasil gabungan
plt.subplot(2, 2, 4)
plt.title('Combined Result')
plt.imshow(dmg, cmap='gray')

# Menampilkan plot
plt.show()
