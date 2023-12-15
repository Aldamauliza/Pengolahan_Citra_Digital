# geomops.py
import numpy as np
import imageio
import cv2

def GeoFun(outcoord):
    a = 10 * np.cos(outcoord[0] / 10.) + outcoord[0]
    b = 10 * np.cos(outcoord[1] / 10.) + outcoord[1]
    return a, b

# Program utama
import scipy.ndimage as nd

# Membaca gambar sebagai grayscale dengan mode='L'
amg = imageio.imread('citra.jpg', pilmode='L')

# Menggunakan geometric_transform dengan GeoFun
bmg = nd.geometric_transform(amg, GeoFun)

# Menampilkan hasil menggunakan OpenCV
cv2.imshow('Transformed Image', bmg.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
