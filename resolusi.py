import numpy as np
import imageio.v2 as imageio

def reduce_intensity_resolution(image_path, bit_mask, output_path):
    # Membaca gambar dan mengonversinya ke skala abu-abu
    img_data = imageio.imread(image_path, mode='L').astype(np.uint8)

    # Mengurangi resolusi intensitas menggunakan bitwise AND dengan bit_mask
    reduced_data = img_data & bit_mask

    # Menyimpan gambar yang sudah diubah ke file
    imageio.imsave(output_path, reduced_data)

    # Mengembalikan data yang telah dikurangi intensitas resolusinya
    return reduced_data

# Path gambar yang ingin diubah (pastikan file 'contoh.jpg' ada di direktori yang benar)
image_path = 'citra.jpg'

# Bit mask yang digunakan untuk mengurangi intensitas resolusi
bit_mask1 = 0xF0
bit_mask2 = 0xC0
bit_mask3 = 0x80

# Output path untuk gambar yang sudah diubah
output_path1 = 'contohF0.png'
output_path2 = 'contohC0.png'
output_path3 = 'contoh80.png'

# Mengurangi intensitas resolusi menggunakan fungsi yang telah dibuat
reduced_data1 = reduce_intensity_resolution(image_path, bit_mask1, output_path1)
reduced_data2 = reduce_intensity_resolution(image_path, bit_mask2, output_path2)
reduced_data3 = reduce_intensity_resolution(image_path, bit_mask3, output_path3)

# Menampilkan ukuran gambar yang sudah diubah
print(reduced_data1.size)
