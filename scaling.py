import imageio.v2 as imageio
import scipy.ndimage as nd
import os

fname = 'citra.jpg'
data = imageio.imread(fname)

#Menampilkan ukuran citra asli
print("Ukuran Citra Asli:", data.shape)

#Scalling citra dengan faktor 2 di semua dimensi
data2 = nd.zoom(data, 2)
print("Ukuran citra setelah scalling dengan faktor 2 di semua dimensi:", data2.shape)

#Scalling citra dengan faktor 2 hanya pada dua diemensi pertama 
data2 = nd.zoom(data, (2, 2, 1))
print("Ukuran citra setelah scalling dengan faktor 2 hanya pada dua dimensi pertama", data2.shape)

#Scalling citra dengan faktor yang berbeda pada setiap dimensi
data3 = nd.zoom(data, (0.5, 0.9, 1))
print("Ukuran citra setelah scaling dengan faktor yang berbeda pada setiap dimensi:", data3.shape)

#Membuat folder output jika belum ada
output = 'output'
if not os.path.exists(output):
    os.makedirs(output)

# Menyimpan citra hasil scaling
imageio.imsave(os.path.join(output, 'zoomed_image.png'), data2)
imageio.imsave(os.path.join(output, 'zoomed_image2.png'), data3)