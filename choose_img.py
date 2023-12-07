import cv2

img_grayscale = cv2.imread('tes.jpeg',0)

print ("Pilih Gambar")
print ("Gambar 1")
print ("Gambar 2")
print ("Gambar 3")

pilih= int(input ("Pilih 1/2/3 :"))

if pilih == 1:
    img_color = cv2.imread('tes.jpeg',cv2.IMREAD_COLOR)
    cv2.imshow('color image',img_color)
    cv2.waitKey(0)
    cv2.destroyAllWindows
elif pilih == 2:
    img_color = cv2.imread('tes.jpeg',cv2.IMREAD_GRAYSCALE)
    cv2.imshow('gratsacel image',img_grayscale)
    cv2.waitKey(0)
    cv2.destroyAllWindows
elif pilih == 3:
    img_unchanged = cv2.imread('tes.jpeg',cv2.IMREAD_UNCHANGED)
    cv2.imshow('unchanged image',img_unchanged)
    cv2.waitKey(0)
    cv2.destroyAllWindows

