import subprocess
import time
import json
import re
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def run_node_commands(start, end, directory, file_prefix, file_extension):
    for i in range(start, end + 1):
        # Construct the file name
        file_number = str(i).zfill(5)
        image_path = os.path.join(directory, f"{file_prefix}{file_number}.{file_extension}")

        # Check if file exists
        if not os.path.isfile(image_path):
            logging.error(f"File not found: {image_path}")
            continue

        # Extract base file name without serial number
        base_file_name = os.path.basename(image_path).split('.')[0][:-5]

        # Construct and run the first command
        mint_command = f"node . mint < Your Inscription Recieving Address Here> {image_path}"
        result_mint = subprocess.run(mint_command, shell=True, capture_output=True, text=True)
        logging.info("Output from mint command:")
        logging.info(result_mint.stdout)

        # Check if there is an error in the first command
        if result_mint.stderr:
            logging.error("Error in mint command:")
            logging.error(result_mint.stderr)

        # Check for specific error message in the first command's output
        if "'64: too-long-mempool-chain'" in result_mint.stdout:
            logging.info("Detected specific error message, proceeding to wallet sync...")

        # Loop for the second command
        max_retries = 6
        retry_count = 0

        while retry_count < max_retries:
            wallet_sync_command = "node . wallet sync"
            result_sync = subprocess.run(wallet_sync_command, shell=True, capture_output=True, text=True)
            logging.info("Output from wallet sync command:")
            logging.info(result_sync.stdout)

            if result_sync.stderr:
                logging.error("Error in wallet sync command:")
                logging.error(result_sync.stderr)

            # Check for success message
            if "inscription txid" in result_sync.stdout:
                logging.info("Successful inscription, extracting txid and updating JSON file.")
                txid = re.search(r"inscription txid: (\w+)", result_sync.stdout).group(1)
                update_json_file(base_file_name, image_path, txid)
                break

            # Check for the specific error and retry
            elif "'64: too-long-mempool-chain'" in result_sync.stdout:
                logging.info(f"Detected specific error message, retrying in 300 seconds (Attempt {retry_count + 1}/{max_retries})")
                time.sleep(300)
                retry_count += 1
            else:
                logging.warning("Unknown response, stopping the retry loop.")
                break

def update_json_file(base_file_name, image_path, txid):
    json_file_name = f"{base_file_name}.json"
    data = {}
    if os.path.isfile(json_file_name):
        with open(json_file_name, 'r') as file:
            data = json.load(file)

    data[os.path.basename(image_path)] = txid

    with open(json_file_name, 'w') as file:
        json.dump(data, file, indent=4)

# Replace with dir to collection.
directory = 'C:\\Doginals-main\\<Doginal-Apes- But Your Collection File Name Here>'
# Replace with collection name. The file name without the serial number.
file_prefix = 'Ape' <File name without the 5 zeros>
# Replace with file extension.
file_extension = 'jpg' < image extension without the period>
# Enter the range of files to inscribe.
start = 1
end = 22
run_node_commands(start, end, directory, file_prefix, file_extension)
