import subprocess
import time
import json
import re
import os

def extract_dogecoin_addresses(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
        addresses = [entry['dogecoin_address'] for entry in data['airDropList']]
        return addresses
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def run_node_commands(start, end, directory, file_prefix, file_extension, addresses):
    file_indices = range(start, end + 1)
    for i, doge_address in zip(file_indices, addresses):
        file_number = str(i).zfill(5)
        image_path = os.path.join(directory, f"{file_prefix}{file_number}.{file_extension}")

        if not os.path.isfile(image_path):
            print(f"File not found: {image_path}")
            continue

        base_file_name = os.path.basename(image_path).split('.')[0][:-5]
        mint_command = f"node . mint {doge_address} {image_path}"
        result_mint = subprocess.run(mint_command, shell=True, capture_output=True, text=True)
        print("Output from mint command:")
        print(result_mint.stdout)

        if result_mint.stderr:
            print("Error in mint command:")
            print(result_mint.stderr)

        txid_search = re.search("inscription txid: (\w+)", result_mint.stdout)
        if txid_search:
            txid = txid_search.group(1)
            print("Successful mint, updating JSON file, continuing in 100 seconds....")
            update_json_file(base_file_name, image_path, txid, doge_address)
            time.sleep(100)
            continue

        if "'64: too-long-mempool-chain'" in result_mint.stdout:
            print("Detected specific error message, proceeding to wallet sync...")
            while True:
                wallet_sync_command = "node . wallet sync"
                result_sync = subprocess.run(wallet_sync_command, shell=True, capture_output=True, text=True)
                print("Output from wallet sync command:")
                print(result_sync.stdout)

                if result_sync.stderr:
                    print("Error in wallet sync command:")
                    print(result_sync.stderr)

                if "inscription txid" in result_sync.stdout:
                    txid = re.search("inscription txid: (\w+)", result_sync.stdout).group(1)
                    update_json_file(base_file_name, image_path, txid, doge_address)
                    break

                elif "'64: too-long-mempool-chain'" in result_sync.stdout:
                    print("Detected specific error message, retrying in 100 seconds...")
                    time.sleep(100)
                else:
                    print("Unknown response, stopping the retry loop.")
                    break


def update_json_file(base_file_name, image_path, txid, doge_address):
    json_file_name = f"{base_file_name}.json"
    data = {}
    if os.path.isfile(json_file_name):
        with open(json_file_name, 'r') as file:
            data = json.load(file)
    
    data[os.path.basename(image_path)] = {"txid": txid, "address": doge_address}

    with open(json_file_name, 'w') as file:
        json.dump(data, file, indent=4)

# Extract Dogecoin addresses from the file
file_name = 'airDropList.json'
addresses = extract_dogecoin_addresses(file_name)

# Replace with your specific details
directory = 'C:\\doginals-main\\RiceCerts'
file_prefix = 'animated'
file_extension = 'webp'
start = 337
end = 351

# Run the modified function
run_node_commands(start, end, directory, file_prefix, file_extension, addresses)
