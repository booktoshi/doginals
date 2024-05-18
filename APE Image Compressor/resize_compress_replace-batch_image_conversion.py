from PIL import Image
import os

def resize_and_compress_image(input_path, output_path, target_size, target_size_kb):
    # Open the image
    image = Image.open(input_path)

    # Resize the image to the target size
    resized_image = image.resize(target_size)

    # Create the output folder if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the resized image
    resized_image.save(output_path, 'JPEG')

    print(f"Resized {input_path} to {output_path} with dimensions {target_size}")

    # Compress the resized image
    compress_image(output_path, output_path, target_size_kb)

def compress_image(input_path, output_path, target_size_kb):
    # Open the image
    image = Image.open(input_path)

    # Convert the image to RGB mode (remove alpha channel)
    image = image.convert('RGB')

    # Set the quality parameter for compression
    quality = 90  # You can adjust this value based on your needs

    # Save the image with compression
    image.save(output_path, 'JPEG', quality=quality, optimize=True)

    print(f"Compressed {input_path} to {output_path} with size {os.path.getsize(output_path) / 1024:.2f} KB")

    # Remove the resized image after compression
    os.remove(input_path)

def batch_resize_and_compress(folder_path, target_size, target_size_kb):
    # Get a list of all image files in the folder
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Process each image file
    for image_file in image_files:
        input_path = os.path.join(folder_path, image_file)
        output_path = os.path.join(folder_path, f"{os.path.splitext(image_file)[0]}_resized_compressed.jpg")

        print("Input Path: " + input_path)
        print("Output Path: " + output_path)

        # Resize and compress the image, and replace the original
        resize_and_compress_image(input_path, output_path, target_size, target_size_kb)

if __name__ == "__main__":
    # Provide the correct path to the folder containing image files
    input_folder = r"C:\Doginals-main\Doginal-Apes"

    # Set the target size for each resized image (500 x 500 pixels)
    target_size = (500, 500)

    # Set the target size for each compressed image in KB
    target_size_kb = 69

    batch_resize_and_compress(input_folder, target_size, target_size_kb)
