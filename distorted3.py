import numpy
import cv2
import math
import os



# Load the image
img = cv2.imread('citra.jpg')

# Grab the dimensions of the image
(h, w, _) = img.shape

# Set up the x and y maps as float32
map_x_convex = numpy.zeros((h, w), numpy.float32)
map_y_convex = numpy.zeros((h, w), numpy.float32)

map_x_concave = numpy.zeros((h, w), numpy.float32)
map_y_concave = numpy.zeros((h, w), numpy.float32)

# Define distortion parameters
scale_x = 1
scale_y = 1
center_x = w/2
center_y = h/2
radius = w/2
amount_convex = 0.95   # Positive values produce barrel
amount_concave = -0.95  # Negative values produce concave

# Create maps with the barrel pincushion distortion formula
for y in range(h):
    delta_y = scale_y * (y - center_y)
    for x in range(w):
        # Determine if the pixel is within an ellipse
        delta_x = scale_x * (x - center_x)
        distance = delta_x * delta_x + delta_y * delta_y

        # Convex distortion
        if distance >= (radius * radius):
            map_x_convex[y, x] = x
            map_y_convex[y, x] = y
        else:
            factor = 1.0
            if distance > 0.0:
                factor = math.pow(math.sin(math.pi * math.sqrt(distance) / radius / 2), amount_convex)
            map_x_convex[y, x] = factor * delta_x / scale_x + center_x
            map_y_convex[y, x] = factor * delta_y / scale_y + center_y

        # Concave distortion
        factor = 1.0
        if distance > 0.0:
            factor = math.pow(math.sin(math.pi * math.sqrt(distance) / radius / 2), amount_concave)
        map_x_concave[y, x] = factor * delta_x / scale_x + center_x
        map_y_concave[y, x] = factor * delta_y / scale_y + center_y

# Do the remap for convex distortion
dst_convex = cv2.remap(img, map_x_convex, map_y_convex, cv2.INTER_LINEAR)

# Do the remap for concave distortion
dst_concave = cv2.remap(img, map_x_concave, map_y_concave, cv2.INTER_LINEAR)

# Create the output folder if it doesn't exist
output_folder = '/output'
os.makedirs(output_folder, exist_ok=True)

# Save the results
cv2.imwrite(os.path.join(output_folder, 'Barrel_distortion.jpg'), dst_convex)
cv2.imwrite(os.path.join(output_folder, 'pincushion_distortion.jpg'), dst_concave)

# Show the results
cv2.imshow('Original', img)
cv2.imshow('barrel Distortion', dst_convex)
cv2.imshow('pincushion Distortion', dst_concave)

cv2.waitKey(0)
cv2.destroyAllWindows()
