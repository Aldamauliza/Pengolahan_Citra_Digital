import numpy as np
import cv2 as cv
import math
import os

def barrel_distortion(img, amount_convex):
    # Grab the dimensions of the image
    (h, w, _) = img.shape

    # Set up the x and y maps as float32
    map_x = np.zeros((h, w), np.float32)
    map_y = np.zeros((h, w), np.float32)

    # Define distortion parameters
    scale_x = 1
    scale_y = 1
    center_x = w/2
    center_y = h/2
    radius = w/2

    # Create maps with the barrel distortion formula
    for y in range(h):
        delta_y = scale_y * (y - center_y)
        for x in range(w):
            # Determine if the pixel is within an ellipse
            delta_x = scale_x * (x - center_x)
            distance = delta_x * delta_x + delta_y * delta_y

            factor = 1.0
            if distance > 0.0:
                factor = math.pow(math.sin(math.pi * math.sqrt(distance) / radius / 2), amount_convex)

            map_x[y, x] = factor * delta_x / scale_x + center_x
            map_y[y, x] = factor * delta_y / scale_y + center_y

    # Do the remap for the barrel distortion
    distorted_img = cv.remap(img, map_x, map_y, cv.INTER_LINEAR)

    return distorted_img

def pincushion_distortion(img, amount_concave):
    # Grab the dimensions of the image
    (h, w, _) = img.shape

    # Set up the x and y maps as float32
    map_x = np.zeros((h, w), np.float32)
    map_y = np.zeros((h, w), np.float32)

    # Define distortion parameters
    scale_x = 1
    scale_y = 1
    center_x = w/2
    center_y = h/2
    radius = w/2

    # Create maps with the pincushion distortion formula
    for y in range(h):
        delta_y = scale_y * (y - center_y)
        for x in range(w):
            # Determine if the pixel is within an ellipse
            delta_x = scale_x * (x - center_x)
            distance = delta_x * delta_x + delta_y * delta_y

            factor = 1.0
            if distance > 0.0:
                factor = math.pow(math.sin(math.pi * math.sqrt(distance) / radius / 2), amount_concave)

            map_x[y, x] = factor * delta_x / scale_x + center_x
            map_y[y, x] = factor * delta_y / scale_y + center_y

    # Do the remap for the pincushion distortion
    distorted_img = cv.remap(img, map_x, map_y, cv.INTER_LINEAR)

    return distorted_img

def main():
    # Load the image
    img = cv.imread('citra.jpg')

    # Display menu
    print("Choose distortion type:")
    print("1. Barrel Distortion (Convex)")
    print("2. Pincushion Distortion (Concave)")
    choice = input("Enter the number (1 or 2): ")

    # Apply the selected distortion
    if choice == '1':
        amount_convex = float(input("Enter the value for convex distortion (e.g., 0.95): "))
        distorted_img = barrel_distortion(img, amount_convex)
    elif choice == '2':
        amount_concave = float(input("Enter the value for concave distortion (e.g., -0.95): "))
        distorted_img = pincushion_distortion(img, amount_concave)
    else:
        print("Invalid choice. Please enter either 1 or 2.")
        return

    # Display and save the results
    cv.imshow('Original', img)
    cv.imshow('Distorted Image', distorted_img)

    # Create the output folder if it doesn't exist
    output_folder = 'PENGERJAAN MODUL/output'
    os.makedirs(output_folder, exist_ok=True)

    # Save the results
    distortion_type = 'barrel' if choice == '1' else 'pincushion'
    cv.imwrite(os.path.join(output_folder, f'{distortion_type}_distortion.jpg'), distorted_img)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "_main_":
    main()