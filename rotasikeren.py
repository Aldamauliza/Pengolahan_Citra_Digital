import cv2

image = cv2.imread("citra.jpg")
data = int(input("Data center:"))

def r_image (image):
    return
height, width = image.shape[:2]
center = (width / data, height / data)
rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=10, scale=1)
rotated_image = cv2.warpAffine(src=image, M=rotate_matrix, dsize=(width, height))



cv2.imshow("Original image", image)
cv2.imshow("Rotated image", rotated_image)
cv2.waitKey(0)
cv2.imwrite("rotated_image.jpg", rotated_image)


