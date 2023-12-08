import imageio
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import map_coordinates


print ("Pilih operasi:")
print ("1. Log Polar")
print ("2. Radial Polar")

pilih= int(input ("Pilih 1/2 :"))

if pilih == 1:
    pxy1, pxy2 = map(int, input("Masukkan dua koordinat dipisahkan oleh spasi: ").split())
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
    pxy = (pxy1, pxy2)

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

elif pilih == 2:
    pxy3, pxy4 = map(int, input("Masukkan dua koordinat dipisahkan oleh spasi: ").split())
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
    pxy = (pxy3, pxy4)

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

