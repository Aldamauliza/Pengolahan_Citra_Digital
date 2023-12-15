# geomops1.py
import numpy as np
import scipy.ndimage as nd
import imageio
import cv2

def AffineExample(data):
    theta = 11 * np.pi / 180  # 11 degrees in radians
    mat = np.array([[np.cos(theta), -np.sin(theta), 0],
                    [np.sin(theta), np.cos(theta), 0],
                    [0, 0, 1]])  # Add a 3rd row and column to make it a 3x3 matrix
    data2 = nd.affine_transform(data, mat)
    return data2

# Program utama
mg2 = AffineExample(imageio.imread('citra.jpg', pilmode='L'))

# Menampilkan hasil menggunakan OpenCV
cv2.imshow('Original Image', imageio.imread('citra.jpg').astype(np.uint8))
cv2.imshow('Transformed Image', mg2.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
