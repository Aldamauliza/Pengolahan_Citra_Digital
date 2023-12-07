import cv2
import numpy as np

# Fungsi untuk mengubah ukuran gambar
def resize_image(input_image_path, output_image_path, new_width, new_height, interpolation=cv2.INTER_LINEAR):
    image = cv2.imread(input_image_path)
    resized_image = cv2.resize(image, (new_width, new_height), interpolation=interpolation)
    cv2.imwrite(output_image_path, resized_image)
    print(f'Gambar yang sudah diubah dengan interpolasi {interpolation} telah disimpan di {output_image_path}')

# Path gambar masukan
input_image_path = 'tes.jpeg'

# Ukuran baru yang diinginkan
down_width = 300
down_height = 200
up_width = 600
up_height = 400

# Pilihan jenis interpolasi
print("Pilih jenis interpolasi:")
print("1. INTER_NEAREST")
print("2. INTER_LINEAR (default)")
print("3. INTER_CUBIC")
choice = int(input("Masukkan nomor pilihan: "))

if choice == 1:
    interpolation = cv2.INTER_NEAREST
elif choice == 2:
    interpolation = cv2.INTER_LINEAR
elif choice == 3:
    interpolation = cv2.INTER_CUBIC
else:
    print("Pilihan tidak valid, menggunakan interpolasi LINEAR sebagai default")
    interpolation = cv2.INTER_LINEAR

# Nama file keluaran
output_downscaled_path = f'img_downscaled.jpg'
output_upscaled_path = f'img_upscaled.jpg'

# Mengubah ukuran gambar dengan jenis interpolasi yang dipilih
resize_image(input_image_path, output_downscaled_path, down_width, down_height, interpolation)
resize_image(input_image_path, output_upscaled_path, up_width, up_height, interpolation)

# Menampilkan pesan sukses
print(f'Gambar yang sudah diubah dengan interpolasi {interpolation} telah disimpan di {output_downscaled_path}')
print(f'Gambar yang sudah diubah dengan interpolasi {interpolation} telah disimpan di {output_upscaled_path}')