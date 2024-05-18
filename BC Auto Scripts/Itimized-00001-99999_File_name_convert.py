import os

def rename_files(folder_path):
    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Define the starting index for numbering
    start_index = 1

    # Iterate through each file and rename
    for file_name in files:
        file_extension = os.path.splitext(file_name)[1]
        new_name = f"{os.path.splitext(file_name)[0]}{start_index:05d}{file_extension}"

        # Construct the full paths
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)

        # Increment the index
        start_index += 1

if __name__ == "__main__":
    # Provide the correct path to the folder containing files
    folder_path = r"C:\Doginals-main\Doginal-Apes_BUT-YOUR-COLLECTION_HERE"

    # Call the function to rename files
    rename_files(folder_path)

    print("Files renamed successfully.")
