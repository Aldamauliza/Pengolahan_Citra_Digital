import numpy as np
import matplotlib.pyplot as plt

V = 128  # Ganti dengan nilai yang diinginkan untuk V
H = 128  # Ganti dengan nilai yang diinginkan untuk H
data = np.zeros((128, 128))
data[0:128:2] = 1
data[:, :128:2] += 1
# Melakukan downsampling menggunakan slicing
b = data[0:V:2, 0:H:2]
c = data[1:V:2, 0:H:2]
d = data[0:V:2, 1:H:2]
f = data[1:V:2, 1:H:2]
# Menggabungkan gambar hasil downsampling
g = np.concatenate((b, c))
h = np.concatenate((d, f))
m = np.concatenate((g, h), axis=1)
# Menampilkan gambar asli dan hasil downsampling
plt.figure(figsize=(8, 4))

plt.subplot(2, 2, 1)
plt.imshow(data, cmap='gray')
plt.title('Gambar Asli')

plt.subplot(2, 2, 2)
plt.imshow(b, cmap='gray')
plt.title('Gambar Hasil Downsampling b')

plt.subplot(2, 2, 3)
plt.imshow(d, cmap='gray')
plt.title('Gambar Hasil Downsampling d')

plt.subplot(2, 2, 4)
plt.imshow(m, cmap='gray')
plt.title('Gabungan Gambar (g, h)')

plt.tight_layout()
plt.show()
