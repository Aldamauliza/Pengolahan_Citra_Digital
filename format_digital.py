from PIL import Image

def read_image(image_path):
    return Image.open(image_path)

def save_image(image, output_path, format):
    image.save(output_path, format=format)
    print(f"Image saved as {output_path} with format: {format}")

def analyze_image(image):
    width, height = image.size
    mode = image.mode
    print(f"Image Information:")
    print(f"  Size: {width} x {height}")
    print(f"  Mode: {mode}")

def compress_bitmap(input_path, output_path):
    image = read_image(input_path)
    save_image(image, output_path, format="BMP")

def compress_jpeg(input_path, output_path):
    image = read_image(input_path)
    save_image(image, output_path, format="JPEG")

def compress_gif(input_path, output_path):
    image = read_image(input_path)
    save_image(image, output_path, format="GIF")

def compress_tiff(input_path, output_path):
    image = read_image(input_path)
    save_image(image, output_path, format="TIFF")

def compress_png(input_path, output_path):
    image = read_image(input_path)
    save_image(image, output_path, format="PNG")

def main():
    input_image_path = "D:/DATA ALDA/Materi Kuliah/SEMESTER 5/Pengolahan Citra Digital/citra.jpg"
    
    while True:
        print("\nMenu:")
        print("1. Compress with BMP")
        print("2. Compress with JPEG")
        print("3. Compress with GIF")
        print("4. Compress with TIFF")
        print("5. Compress with PNG")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            output_path = "D:/DATA ALDA/Materi Kuliah/SEMESTER 5/Pengolahan Citra Digital/compressed_image.bmp"
            compress_bitmap(input_image_path, output_path)
            analyze_image(read_image(output_path))
        elif choice == "2":
            output_path = "D:/DATA ALDA/Materi Kuliah/SEMESTER 5/Pengolahan Citra Digital/compressed_image.jpg"
            compress_jpeg(input_image_path, output_path)
            analyze_image(read_image(output_path))
        elif choice == "3":
            output_path = "D:/DATA ALDA/Materi Kuliah/SEMESTER 5/Pengolahan Citra Digital/compressed_image.gif"
            compress_gif(input_image_path, output_path)
            analyze_image(read_image(output_path))
        elif choice == "4":
            output_path = "D:/DATA ALDA/Materi Kuliah/SEMESTER 5/Pengolahan Citra Digital/compressed_image.tiff"
            compress_tiff(input_image_path, output_path)
            analyze_image(read_image(output_path))
        elif choice == "5":
            output_path = "D:/DATA ALDA/Materi Kuliah/SEMESTER 5/Pengolahan Citra Digital/compressed_image.png"
            compress_png(input_image_path, output_path)
            analyze_image(read_image(output_path))
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
