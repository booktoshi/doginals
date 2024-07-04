import subprocess
import time
import json
import re
import os
from tqdm import tqdm

def extract_number_from_filename(filename):
    # Extract the number after '#' in the filename
    match = re.search(r'#(\d+)', filename)
    if match:
        return int(match.group(1))
    else:
        return 0  # Default to 0 if no number found

def get_wallet_address():
    wallet_address = input("Please enter the wallet address to send the inscriptions to: ")
    return wallet_address

def scan_directory(directory):
    base_directory = f'./{directory}'
    if not os.path.exists(base_directory):
        print(f"Directory {base_directory} does not exist.")
        return []

    files = []
    for file_name in os.listdir(base_directory):
        if not file_name.startswith('.') and os.path.isfile(os.path.join(base_directory, file_name)):
            files.append(os.path.join(base_directory, file_name))
    
    return files

def list_file_types(files):
    file_types = set()
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        file_types.add(ext)
    
    return file_types

def confirm_file_count(files):
    count = len(files)
    print(f"Found {count} files in the directory.")
    confirmation = input(f"Is this the correct number of files to process? (yes/no): ").strip().lower()
    return confirmation == 'yes'

def ask_batch_processing():
    process_in_batches = input("Would you like to process the files in batches? (yes/no): ").strip().lower()
    if process_in_batches == 'yes':
        batch_size = int(input("How many files should the script process before pausing for 100 seconds (max 12 for HTML files)?: ").strip())
        batch_size = min(batch_size, 12)  # Ensure no more than 12 HTML files are batched
        return True, batch_size
    else:
        return False, None

def print_colored(text, fg_color, bg_color):
    # Print colored text using ANSI escape codes
    print(f"\033[38;2;{fg_color[0]};{fg_color[1]};{fg_color[2]}m\033[48;2;{bg_color[0]};{bg_color[1]};{bg_color[2]}m{text}\033[0m")

def run_node_commands(directory):
    files = scan_directory(directory)

    if not files:
        print(f"No files found in {directory}.")
        return

    file_types = list_file_types(files)
    print(f"File types found in the directory: {', '.join(file_types)}")

    if not confirm_file_count(files):
        print("Please check the files in the directory and try again.")
        return

    wallet_address = get_wallet_address()

    process_in_batches, batch_size = ask_batch_processing()

    # Sort files based on the number after '#'
    files.sort(key=lambda x: extract_number_from_filename(os.path.basename(x)))

    # Ensure metadata directory exists
    metadata_directory = './metadata'
    if not os.path.exists(metadata_directory):
        os.makedirs(metadata_directory)

    # Create or load inscriptionIDs.json in the metadata directory
    json_file_name = os.path.join(metadata_directory, "inscriptionIDs.json")
    if not os.path.isfile(json_file_name):
        with open(json_file_name, 'w') as file:
            json.dump([], file)

    total_processed = 0

    # Set up progress bar
    fg_color = (255, 204, 0)  # FFCC00
    bg_color = (51, 51, 51)   # 333333
    pbar = tqdm(total=len(files), bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]")
    pbar.bar_format = "{l_bar}\033[38;2;255;204;0m{bar}\033[0m| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]"

    while total_processed < len(files):
        if process_in_batches:
            batch_files = files[total_processed:total_processed + batch_size]
            print(f"\nProcessing batch {total_processed // batch_size + 1}")
        else:
            # Check for HTML files when not batching
            if any(f.lower().endswith('.html') for f in files):
                print("HTML files found. The script cannot proceed without batching.")
                break
            batch_files = files[total_processed:]
        
        for index, file_path in enumerate(batch_files, start=1):
            total_file_index = total_processed + index
            total_file_count = len(files)
            print(f"\nProcessing file {total_file_index} of {total_file_count}: {file_path}")

            # Attempt to mint the file
            success = False
            while not success:
                # Construct and run the mint command
                mint_command = f"node . mint {wallet_address} {file_path}"
                result_mint = subprocess.run(mint_command, shell=True, capture_output=True, text=True)
                print("Output from mint command:")
                print(result_mint.stdout)

                # Check if there is an error in the mint command
                if result_mint.stderr:
                    print("Error in mint command:")
                    print(result_mint.stderr)

                # Check for success message in the mint command's output
                txid_search = re.search("inscription txid: (\w+)", result_mint.stdout)
                if txid_search:
                    txid = txid_search.group(1)
                    print("Successful mint, updating JSON file...")
                    update_json_file(json_file_name, file_path, txid)
                    success = True
                else:
                    # Check for specific error message in the mint command's output
                    if "'64: too-long-mempool-chain'" in result_mint.stdout:
                        print("Detected specific error message, waiting for 100 seconds...")
                        time.sleep(100)
                    else:
                        print("Failed to mint file, retrying...")

            pbar.update(1)

            if process_in_batches and total_file_index % batch_size == 0:
                print(f"Processed {batch_size} files, taking a 100-second break...")
                time.sleep(100)

        total_processed += len(batch_files)
        if not process_in_batches:
            break

    pbar.close()
    print_colored("All files processed.", fg_color, bg_color)

def update_json_file(json_file_name, file_path, txid):
    # Load existing data
    with open(json_file_name, 'r') as file:
        data = json.load(file)

    # Append new data
    data.append({
        "inscriptionId": txid,
        "name": os.path.basename(file_path),
        "file_name": os.path.basename(file_path),
        "attributes": {
            "trait1": "trait1",
            "trait2": "trait2",
            "trait3": "trait3",
            "trait4": "trait4",
            "trait5": "trait5",
            "trait6": "trait6",
            "trait7": "trait7"
        }
    })

    # Write back to JSON file
    with open(json_file_name, 'w') as file:
        json.dump(data, file, indent=4)

# Run the script with 'files' directory containing various files
run_node_commands('files')
