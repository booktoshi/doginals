import subprocess
import time
import json
import re
import os
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# Setup environment variables and RPC connection
rpc_user = os.getenv('RPC_USER', 'your_rpc_user')
rpc_password = os.getenv('RPC_PASSWORD', 'veracity31')
rpc_host = os.getenv('RPC_HOST', 'localhost')
rpc_port = os.getenv('RPC_PORT', '22555')
rpc_connection = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}/")

def read_last_output(json_file_name):
    """Read and return the number of processed transactions from JSON."""
    try:
        if os.path.exists(json_file_name):
            with open(json_file_name, 'r') as file:
                data = json.load(file)
                print(f"Read data: {data}")
                return len(data)
    except json.JSONDecodeError as e:
        print(f"JSON decode error in {json_file_name}: {e}")
    return 0

def extract_details(file_name):
    """Extract air drop details from JSON file."""
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(f"Extracted details: {data.get('airDropList', [])}")
            return data.get('airDropList', [])
    except Exception as e:
        print(f"An error occurred while reading {file_name}: {e}")
        return []

def update_json_file(image_path, txid, details):
    """Update JSON file with transaction details."""
    json_file_name = "recursiveCollection001Output.json"
    try:
        data = {}
        if os.path.exists(json_file_name):
            with open(json_file_name, 'r') as file:
                data = json.load(file)
        key = os.path.basename(image_path)
        data[key] = {"txid": txid, "address": details['address']}
        with open(json_file_name, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Updated JSON file {json_file_name} with: {data[key]}")
    except Exception as e:
        print(f"Error updating {json_file_name}: {e}")

def process_mint_batch(start, end, directory, file_prefix, file_extension, details_list):
    """Process minting for a batch of transactions."""
    last_txid = ""
    for i in range(start, end + 1):
        if i > len(details_list):
            break
        details = details_list[i - 1]
        file_number = str(i).zfill(5)
        image_path = os.path.join(directory, f"{file_prefix}{file_number}.{file_extension}")
        if not os.path.exists(image_path):
            print(f"File not found: {image_path}")
            continue
        mint_command = f"node . mint {details['address']} {image_path}"
        print(f"Executing command: {mint_command}")
        result_mint = subprocess.run(mint_command, shell=True, capture_output=True, text=True)
        print("Output from mint command:", result_mint.stdout)
        if result_mint.stderr:
            print("Error in mint command:", result_mint.stderr)
        txid_search = re.search("inscription txid: (\\w+)", result_mint.stdout)
        if txid_search:
            last_txid = txid_search.group(1)
            print(f"Successful mint, TXID: {last_txid}")
            update_json_file(image_path, last_txid, details)
    return last_txid

def wait_for_tx_confirmation(txid):
    """Wait for a transaction to be confirmed."""
    retries = 500  # Number of retries
    while retries > 0:
        try:
            tx_info = rpc_connection.gettransaction(txid)
            if tx_info and tx_info.get("confirmations", 0) >= 1:
                print(f"Transaction {txid} is confirmed.")
                return  # Exit the function if transaction is confirmed
        except JSONRPCException as e:
            print(f"Error fetching transaction {txid}: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        retries -= 1
        time.sleep(10)  # Wait for a few seconds before retrying
    print(f"Failed to confirm transaction {txid} after multiple retries.")

def continuous_minting_process(directory, file_prefix, file_extension):
    """Main processing function to handle minting in continuous mode."""
    last_count = read_last_output('recursiveCollection001Output.json')
    details_list = extract_details('airDropList.json')
    if last_count >= len(details_list):
        print("No more details to process or index out of bounds.")
        return
    batch_size = 12
    num_batches = (len(details_list) + batch_size - 1) // batch_size
    for batch_index in range(num_batches):
        start_index = batch_index * batch_size
        end_index = start_index + batch_size - 1
        if end_index >= len(details_list):
            end_index = len(details_list) - 1
        print(f"Processing batch from file {last_count + start_index + 1} to {last_count + end_index + 1}")
        last_txid = process_mint_batch(last_count + start_index + 1, last_count + end_index + 1, directory, file_prefix, file_extension, details_list)
        if last_txid:
            print(f"Waiting for confirmation of TXID: {last_txid}")
            wait_for_tx_confirmation(last_txid)
        else:
            print("No valid transactions in this batch to wait for.")

# Initialize main variables and start the process
directory = r'C:\doginals-main\recurciveCollectionGen\HTMLs'
file_prefix = 'recurcive_collection_001'
file_extension = 'html'

continuous_minting_process(directory, file_prefix, file_extension)
