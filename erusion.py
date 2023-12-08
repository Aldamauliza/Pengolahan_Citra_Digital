import cv2
import numpy as np
import matplotlib.pyplot as plt

# Membaca gambar dengan mode 'grayscale'
img = cv2.imread('citra.jpg', cv2.IMREAD_GRAYSCALE)

# Mengaplikasikan binary thresholding
_, thresholded_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Membuat kernel untuk operasi erosion
kernel = np.ones((5, 5), np.uint8)

# Melakukan operasi erosion
eroded_img = cv2.erode(thresholded_img, kernel, iterations=1)

# Menampilkan hasil
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(thresholded_img, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Eroded Image')
plt.imshow(eroded_img, cmap='gray')

plt.show()