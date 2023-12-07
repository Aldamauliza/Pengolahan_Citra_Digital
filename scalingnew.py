import imageio.v2 as imageio
import scipy.ndimage as nd

fname = 'citra.jpg'
data = imageio.imread(fname)

# Menampilkan ukuran citra asli
print("Ukuran citra asli:", data.shape)

# Scaling citra dengan faktor 2 di semua dimensi
data2 = nd.zoom(data, 2)
print("Ukuran citra setelah scaling dengan faktor 2 di semua dimensi:", data2.shape)

# Scaling citra dengan faktor 2 hanya pada dua dimensi pertama
data2 = nd.zoom(data, (2, 2, 1))
print("Ukuran citra setelah scaling dengan faktor 2 hanya pada dua dimensi pertama:", data2.shape)

# Scaling citra dengan faktor yang berbeda pada setiap dimensi
data2 = nd.zoom(data, (0.5, 0.9, 1))
print("Ukuran citra setelah scaling dengan faktor yang berbeda pada setiap dimensi:", data2.shape)

# Menyimpan citra hasil scaling
imageio.imsave('zoomed_image.png', data2)
