## PNG-Image-Compression-Script
"Image Compression Script in Python"  This repository contains a Python script utilizing the Pillow library to compress PNG images efficiently. Reduce the size of your images while maintaining quality, making them suitable for web applications and storage. Customize compression parameters to your needs.

# Image Compression Script

This script is designed to compress PNG images in a specified folder to a target size using Python's Pillow (PIL) library.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/GreatApe42069/image-resize-compress-replace.git

2. **Navigate to the Script Directory:**

`cd your-repository`

3. **Install Dependencies:
Make sure to install the required dependencies using:**

`pip install Pillow`

4. **Adjust Parameters:**

*Open the `compress_images.py` script and update the following parameters:*

`input_folder`: Provide the correct path to the folder containing PNG files.
`target_size_kb`: Set the target size for each compressed image in kilobytes.

5. **Run the Script:**

*Execute the script using the following command:*

`python compress_images.py`

## Parameters
`input_folder` (str):
Provide the path to the folder containing PNG files that need compression.

`target_size_kb` (int):
Set the target size for each compressed image in kilobytes.

**Notes:**
The script uses the Pillow library for image processing.
Adjust the `quality` parameter in the script for compression based on your needs.
The compressed images will be saved in the 'compressed' subfolder.

## Example:
`python compress_images.py`

This will compress PNG images in the specified folder and save the compressed versions in the 'compressed' subfolder.


Be sure to customize the script parameters and usage instructions according to your specific requirements.

