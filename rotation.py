import cv2
 
# Reading the image
image = cv2.imread('tes.jpeg')

# Dividing height and width by 2 to get the center of the image
height, width = image.shape[:2]
center = (width/2, height/2)

# the above center is the center of rotation axis
# use cv2.getRotationMatrix2D() to get the rotation matrix
rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=45, scale=1)

# Rotate the image using cv2.warpAffine
rotated_image = cv2.warpAffine(src=image, M=rotate_matrix, dsize=(width, height))

# visualize the original and the rotated image
cv2.imshow('Original image', image)
cv2.imshow('Rotated image', rotated_image)
# wait indefinitely, press any key on keyboard to exit
cv2.waitKey(0)
# write the output, the rotated image to disk
cv2.imwrite('rotated_image.jpg', rotated_image)

