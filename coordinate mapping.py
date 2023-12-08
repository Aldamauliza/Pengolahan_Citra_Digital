import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

# Fungsi untuk membuat matriks pemetaan M0 sesuai dengan persamaan (6.24)
def create_mapping_matrix(size, max_distance, translation_point):
    v, h = np.indices(size)
    d = np.random.uniform(-max_distance, max_distance, size)
    M0 = np.array([v + 2 * d * size[0] - d, h + 2 * d * size[1] - d])

    # Tambahkan titik transformasi translasi
    M0[0] += translation_point[0]
    M0[1] += translation_point[1]

    return M0.astype(int)

# Fungsi untuk melakukan transformasi citra sesuai dengan persamaan (6.25)
def apply_mapping(image, M):
    output_image = ndimage.map_coordinates(image, M, order=1, mode='nearest')
    return output_image

# Load citra sebagai citra grayscale
input_image = plt.imread('citra.jpg')[:,:,0]

# Buat matriks identitas sebagai matriks pemetaan awal
identity_mapping = np.indices(input_image.shape)

# Tentukan jarak maksimum perpindahan
max_travel_distance = 0

# Tentukan titik transformasi translasi
translation_point = (50, 150)  # Geser citra 5 piksel ke kanan dan 5 piksel ke bawah

# Buat matriks pemetaan M0 menggunakan fungsi yang telah dibuat
mapping_matrix = create_mapping_matrix(input_image.shape, max_travel_distance, translation_point)

# Aplikasikan transformasi citra
output_image = apply_mapping(input_image, mapping_matrix)

# Tampilkan citra hasil transformasi
plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.imshow(input_image, cmap='gray')
plt.title('Citra Awal')

plt.subplot(1, 2, 2)
plt.imshow(output_image, cmap='gray')
plt.title('Citra Hasil Transformasi')

plt.show()
