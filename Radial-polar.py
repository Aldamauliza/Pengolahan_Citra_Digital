import imageio
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import map_coordinates

def IRPolar(rpdata, pxy):
    ndx = np.indices(rpdata.shape)
    ndx[0] -= pxy[0]
    ndx[1] -= pxy[1]
    v, h = rpdata.shape
    r = np.sqrt(ndx[0]**2 + ndx[1]**2)
    theta = np.arctan2(-ndx[0], -ndx[1]) / (2 * np.pi) * h
    ndx[0] = r.astype(int)
    ndx[1] = theta.astype(int) + h // 2
    answ = map_coordinates(rpdata, ndx)
    answ[pxy[0], pxy[1]:] = answ[pxy[0] - 1, pxy[1]:]
    return answ

# Baca gambar dari file
gambar_asli = imageio.imread('citra.jpg', mode='L')

# Koordinat pergeseran
pxy = (10, 10)

# Terapkan transformasi radial
rpdata = IRPolar(gambar_asli, pxy)

# Ubah ukuran gambar
fig, axes = plt.subplots(1, 2, figsize=(12, 5))  # Set the number of subplots to 2

# Tampilkan gambar menggunakan matplotlib
axes[0].imshow(gambar_asli, cmap='gray')
axes[0].set_title('Gambar Asli')

axes[1].imshow(rpdata.reshape(gambar_asli.shape), cmap='gray')
axes[1].set_title('Gambar Hasil Transformasi Radial')

plt.show()

