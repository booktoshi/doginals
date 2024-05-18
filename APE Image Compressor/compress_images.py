from PIL import Image
import os

def compress_image(input_path, output_path, target_size_kb):
    # Open the image
    image = Image.open(input_path)

    # Convert the image to RGB mode (remove alpha channel)
    image = image.convert('RGB')

    # Set the quality parameter for compression
    quality = 85  # You can adjust this value based on your needs

    # Create the output folder if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the image with compression
    image.save(output_path, 'JPEG', quality=quality, optimize=True)

    print(f"Compressed {input_path} to {output_path} with size {os.path.getsize(output_path) / 1024:.2f} KB")

# ... (rest of the script remains unchanged)

def batch_compress(folder_path, target_size_kb):
    # Get a list of all PNG files in the folder
    png_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.png')]

    # Create output folder if it doesn't exist
    output_folder = os.path.join(folder_path, 'compressed')
    os.makedirs(output_folder, exist_ok=True)

    # Process each PNG file
    for png_file in png_files:
        input_path = os.path.join(folder_path, png_file)
        output_path = os.path.join(output_folder, f"{os.path.splitext(png_file)[0]}_compressed.jpg")

        print("Input Path: " + input_path)
        print("Output Path: " + output_path)

        compress_image(input_path, output_path, target_size_kb)

if __name__ == "__main__":
    # Provide the correct path to the folder containing PNG files
    input_folder = r"C:\Doginals-main\Doginal-Apes"

    # Set the target size for each compressed image in KB
    target_size_kb = 60

    batch_compress(input_folder, target_size_kb)
