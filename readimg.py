import cv2

img_grayscale = cv2.imread('tes.jpeg',0)

img_color = cv2.imread('tes.jpeg',cv2.IMREAD_COLOR)
img_color = cv2.imread('tes.jpeg',cv2.IMREAD_GRAYSCALE)
img_unchanged = cv2.imread('tes.jpeg',cv2.IMREAD_UNCHANGED)

cv2.imshow('color image',img_color)
cv2.imshow('gratsacel image',img_grayscale)
cv2.imshow('unchanged image',img_unchanged)

cv2.waitKey(0)

cv2.destroyAllWindows