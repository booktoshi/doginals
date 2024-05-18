from PIL import Image, PngImagePlugin
import json
import os

def read_metadata(image_path):
    with Image.open(image_path) as img:
        # Check if the image has metadata
        if "Metadata" in img.info:
            metadata = img.info["Metadata"]
            metadata_dict = json.loads(metadata)
            print("Metadata found in the image:")

            # Print base image resolution
            base_image_resolution = metadata_dict.get("base_image_resolution", {})
            print(f"Base Image Resolution: {base_image_resolution}")

            # Print trait details
            attributes = metadata_dict.get("attributes", {})
            for trait_type, details in attributes.items():
                print(f"Trait Type: {trait_type}")
                for detail in details:
                    value = detail.get("value", "Unknown")
                    coordinates = detail.get("coordinates", {})
                    x = coordinates.get("x", "Unknown")
                    y = coordinates.get("y", "Unknown")
                    print(f"  Value: {value}, Coordinates: (x: {x}, y: {y})")
        else:
            print("No metadata found in the image.")

if __name__ == "__main__":
    base_dir = os.getcwd()
    image_path = os.path.join(base_dir, "stitched_image.png")
    
    read_metadata(image_path)
