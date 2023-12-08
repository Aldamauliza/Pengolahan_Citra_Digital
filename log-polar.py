import imageio
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import map_coordinates

def LogPolar(data, pxy):
    ndx = np.indices(data.shape)
    v, h = data.shape
    a = ndx[1].astype(float)
    a = a / h * 2 * np.pi
    r = np.exp(ndx[0] / v * np.log(v / 2)) - 1.0
    y = r * np.cos(a)
    x = r * np.sin(a)
    ndx[0] = x.astype(int) + pxy[0]
    ndx[1] = y.astype(int) + pxy[1]
    answ = map_coordinates(data, ndx)
    return answ

# Baca gambar dari file
gambar_asli = imageio.imread('citra.jpg', mode='L')

# Koordinat pergeseran
pxy = (10, 10)

# Terapkan transformasi log-polar
log_polar_data = LogPolar(gambar_asli, pxy)

# Tampilkan gambar menggunakan matplotlib
plt.subplot(1, 2, 1)
plt.imshow(gambar_asli, cmap='gray')
plt.title('Gambar Asli')

plt.subplot(1, 2, 2)
plt.imshow(log_polar_data.reshape(gambar_asli.shape), cmap='gray')
plt.title('Gambar dengan Transformasi Log-Polar')

plt.show()
