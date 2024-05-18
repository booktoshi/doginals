import subprocess
import time
import json
import re
import os

def extract_details(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
        details_list = []
        for entry in data['airDropList']:
            details = {
                'handle': entry['handle'],
                'at': entry['at'],
                'note': entry['note'],
                'dogecoin_address': entry['dogecoin_address']
            }
            details_list.append(details)
        return details_list
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def run_node_commands(start, end, directory, file_prefix, file_extension, details_list):
    file_indices = range(start, end + 1)
    for i, details in zip(file_indices, details_list):
        doge_address = details['dogecoin_address']
        file_number = str(i).zfill(5)
        image_path = os.path.join(directory, f"{file_prefix}{file_number}.{file_extension}")

        if not os.path.isfile(image_path):
            print(f"File not found: {image_path}")
            continue

        base_file_name = os.path.basename(image_path).split('.')[0][:-5]
        mint_command = f"node . mint {doge_address} {image_path}"
        result_mint = subprocess.run(mint_command, shell=True, capture_output=True, text=True)
        

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
            update_json_file(base_file_name, image_path, txid, details)
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
                    update_json_file(base_file_name, image_path, txid, details)
                    break

                elif "'64: too-long-mempool-chain'" in result_sync.stdout:
                    print("Detected specific error message, retrying in 100 seconds...")
                    time.sleep(100)
                else:
                    print("Unknown response, stopping the retry loop.")
                    break


def update_json_file(base_file_name, image_path, txid, details):
    json_file_name = "airDropOutput.json"
    data = {}

    try:
        if os.path.isfile(json_file_name):
            with open(json_file_name, 'r') as file:
                data = json.load(file)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error reading from {json_file_name}: {e}")

    key = os.path.basename(image_path)
    data[key] = {
        "txid": txid,
        "address": details['dogecoin_address'],
        "handle": details['handle'],
        "at": details['at'],
        "note": details['note']
    }

    try:
        with open(json_file_name, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error writing to {json_file_name}: {e}")

file_name = 'airDropList.json'
details_list = extract_details(file_name)

# Replace with your specific details
directory = 'C:\\doginals-main\\RiceCerts\\gifCerts\\redWorm'  #c:\doginals-main\RiceCerts\gifCerts\redWorm
file_prefix = 'smallCert'
file_extension = 'webp'
start = 353
end = 380

# Run the modified function
run_node_commands(start, end, directory, file_prefix, file_extension, details_list)
