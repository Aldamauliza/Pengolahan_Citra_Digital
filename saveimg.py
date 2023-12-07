import cv2
#Untuk mengimport img
img_grayscale = cv2.imread('tes.jpeg', 0)

#Pilih img
print("Pilih Gambar")
print("Gambar 1")
print("Gambar 2")
print("Gambar 3")

pilih = int(input("Pilih 1/2/3: "))

#opsi pilihan 1
if pilih == 1:
    img_color = cv2.imread('tes.jpeg', cv2.IMREAD_COLOR)
    cv2.imshow('color image', img_color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    #menyimpan gambar
    simpan = input("Apakah Anda ingin menyimpan gambar ini? (y/n): ")
    if simpan.lower() == 'y':
        cv2.imwrite('color_image.jpeg', img_color)
elif pilih == 2:
    img_color = cv2.imread('tes.jpeg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('grayscale image', img_grayscale)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    simpan = input("Apakah Anda ingin menyimpan gambar ini? (y/n): ")
    if simpan.lower() == 'y':
        cv2.imwrite('grayscale_image.jpeg', img_grayscale)
elif pilih == 3:
    img_unchanged = cv2.imread('tes.jpeg', cv2.IMREAD_UNCHANGED)
    cv2.imshow('unchanged image', img_unchanged)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    simpan = input("Apakah Anda ingin menyimpan gambar ini? (y/n): ")
    if simpan.lower() == 'y':
        cv2.imwrite('unchanged_image.jpeg', img_unchanged)
