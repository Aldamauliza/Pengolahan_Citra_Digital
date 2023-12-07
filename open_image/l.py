import cv2

img = cv2.imread('Black')

if img is not None and img.shape[0] > 0 and img.shape[1] > 0:
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Gambar tidak valid atau memiliki ukuran nol.")