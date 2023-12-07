import cv2
import numpy as np

# Membaca gambar
image = cv2.imread('monday.jpeg')
cv2.imshow('Original Image', image)

# Meminta input dari pengguna untuk lebar dan tinggi baru
new_width = int(input('Masukkan lebar baru: '))
new_height = int(input('Masukkan tinggi baru: '))

# Mengubah ukuran gambar sesuai dengan input pengguna
resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
