
# Image Stitching and Metadata Handling

This repository contains two Python scripts:

1. `stitch_images.py`: Stitches images from multiple folders into an 8x8 grid and includes metadata.
2. `read_metadata.py`: Reads and prints metadata from the stitched image.

## Requirements

- Python 3.x
- Pillow library

You can install the Pillow library using pip:

```bash
pip install pillow
```

## Usage

### Stitch Images with Metadata

The `stitch_images.py` script stitches images from folders named the number of rows (or any folder with names starting with these digits) into a grid and saves the resulting image with metadata.

1. Ensure your working directory contains the folders named the number of rows with the images. The first character of each folder name is used to determine the row in which the images should be placed. (eg. /1Background, /2backgroungTrait, /3Body, /4bodyTrait)
2. Run the script:

```bash
python stitch_images.py
```

The script will create a `stitched_image.png` file in the same directory with metadata containing the coordinates and filenames of the images used.

### Read and Print Metadata

The `read_metadata.py` script reads and prints the metadata from the `stitched_image.png` file.

1. Ensure `stitched_image.png` is in your working directory.
2. Run the script:

```bash
python read_metadata.py
```

The script will print the metadata, showing the trait type, trait name, and their coordinates.



## License

This project is licensed under the MIT License
