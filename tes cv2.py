import cv2

img_grayscale = cv2.imread('tes.jpeg',0)

cv2.imshow('grayscale image', img_grayscale)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite('grayscale.jpeg', img_grayscale)