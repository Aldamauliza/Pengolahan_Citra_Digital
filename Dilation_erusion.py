import imageio.v2 as imageio
import scipy.ndimage as nd
import cv2
import numpy as np
import matplotlib.pyplot as plt

print ("Pilih operasi:")
print ("Dilation")
print ("Erusion")

pilih= int(input ("Pilih 1/2 :"))

if pilih == 1:
# Membaca gambar dengan mode='F'
    iterations_dilation_1, iterations_dilation_2 = map(int, input("Masukkan dua jumlah iterasi dipisahkan oleh spasi: ").split())
    iterations_dilation_3, iterations_dilation_4 = map(int, input("Masukkan dua jumlah iterasi dipisahkan oleh spasi: ").split())

def dilation ():

    amg = imageio.imread('citra.jpg', mode='F') < 100

    # Melakukan binary dilation dengan iterasi yang berbeda
    bmg = nd.binary_dilation(amg, iterations=iterations_dilation_1) ^ nd.binary_dilation(amg, iterations=iterations_dilation_2)
    cmg = nd.binary_dilation(amg, iterations=iterations_dilation_3) ^ nd.binary_dilation(amg, iterations=iterations_dilation_4)

    # Menggabungkan hasilnya menggunakan operator bitwise OR (`|`)
    dmg = amg | bmg | cmg

    # Menampilkan gambar awal
    plt.subplot(2, 2, 1)
    plt.title('Original Image')
    plt.imshow(amg, cmap='gray')

    # Menampilkan hasil dilasi biner pertama
    plt.subplot(2, 2, 2)
    plt.title('Binary Dilation 1')
    plt.imshow(bmg, cmap='gray')

    # Menampilkan hasil dilasi biner kedua
    plt.subplot(2, 2, 3)
    plt.title('Binary Dilation 2')
    plt.imshow(cmg, cmap='gray')

    # Menampilkan hasil gabungan
    plt.subplot(2, 2, 4)
    plt.title('Combined Result')
    plt.imshow(dmg, cmap='gray')

    # Menampilkan plot
    plt.show()


if pilih == 2:
    erosi = int(input("Masukkan jumlah iterasi: "))

def erusion ():

# Membaca gambar dengan mode 'grayscale'
    img = cv2.imread('citra.jpg', cv2.IMREAD_GRAYSCALE)

    # Mengaplikasikan binary thresholding
    _, thresholded_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # Membuat kernel untuk operasi erosion
    kernel = np.ones((5, 5), np.uint8)

    # Melakukan operasi erosion
    eroded_img = cv2.erode(thresholded_img, kernel, iterations=erosi)

    # Menampilkan hasil
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(thresholded_img, cmap='gray')

    plt.subplot(1, 2, 2)
    plt.title('Eroded Image')
    plt.imshow(eroded_img, cmap='gray')

    plt.show()