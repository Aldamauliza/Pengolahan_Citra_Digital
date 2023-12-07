import cv2

# Load the original image
img = cv2.imread('rabbit.jpg')  # Ganti 'your_image_file.jpg' dengan nama file gambar Anda

# Get the dimensions of the image
height, width, _ = img.shape

# Define the dimensions of the rectangles
rectangle_width = 174  # Lebar persegi panjang
rectangle_height = 289  # Tinggi persegi panjang

# Create a copy of the original image
imageRectangle = img.copy()

# Define the gap between the rectangles
horizontal_gap = 10  # Misalnya, 10 piksel antara setiap persegi panjang secara horizontal
vertical_gap = 10    # Misalnya, 10 piksel antara setiap persegi panjang secara vertikal

# Loop through the image
for y in range(0, height, rectangle_height + vertical_gap):
    for x in range(0, width, rectangle_width + horizontal_gap):
        start_x = x
        start_y = y
        end_x = x + rectangle_width
        end_y = y + rectangle_height

        # Draw the rectangle on the image
        cv2.rectangle(imageRectangle, (start_x, start_y), (end_x, end_y), (0, 0, 255), thickness=3, lineType=cv2.LINE_8)

# Display the output
cv2.imshow('imageRectangle', imageRectangle)
cv2.waitKey(0)