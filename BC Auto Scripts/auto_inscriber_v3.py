import subprocess
import time
import json
import re
import os
import websocket

MAX_RETRIES = 6
BASE_RETRY_DELAY_SECONDS = 300  # Increase to 300 seconds (5 minutes)

# Replace with dir to collection (image files).
image_directory = 'C:\\Doginals-main\\Doginal-Apes'
# Replace with dir where .env file is located.
env_directory = 'C:\\Doginals-main'

def get_mempool_congestion():
    mempool_api_url = 'https://turbo.ordinalswallet.com/wallet/:address'
    try:
        # Establish WebSocket connection
        with websocket.create_connection(mempool_api_url) as ws:
            # Subscribe to mempool updates
            subscribe_message = json.dumps({"op": "unconfirmed_sub"})
            ws.send(subscribe_message)

            # Wait for a response
            response = ws.recv()
            data = json.loads(response)

        return data.get('mempool', {}).get('size', 0)
    except Exception as e:
        print(f"Error fetching mempool congestion: {e}")
        return 0

def calculate_dynamic_delay_and_adjust_fees(congestion, env_directory):
    # Adjust the delay based on mempool congestion
    dynamic_delay = max(BASE_RETRY_DELAY_SECONDS, BASE_RETRY_DELAY_SECONDS * (congestion / 1000))

    # Adjust fees in .env file based on congestion
    adjust_fees_in_env_file(congestion, env_directory)

    return dynamic_delay

def adjust_fees_in_env_file(congestion, env_directory):
    env_file_path = os.path.join(env_directory, '.env')

    # Calculate fees based on congestion levels
    standard_fee = 100000000
    congested_fee = 300000000
    extreme_congestion_fee = 600000000

    # Choose fees based on congestion levels
    if congestion < 500:
        new_fee = standard_fee
    elif 500 <= congestion < 1000:
        new_fee = congested_fee
    else:
        new_fee = extreme_congestion_fee

    # Add code to read and modify the .env file
    with open(env_file_path, 'r') as file:
        lines = file.readlines()

    # Find and update the transaction fee parameter in the .env file
    for i, line in enumerate(lines):
        if line.startswith("FEE_PER_KB="):
            lines[i] = f"FEE_PER_KB={new_fee}\n"
            break

    # Write the modified lines back to the .env file
    with open(env_file_path, 'w') as file:
        file.writelines(lines)

    # Run node sync and wait for changes to take effect
    wallet_sync_command_after_adjustments = "node . wallet sync"
    result_sync_after_adjustments = subprocess.run(wallet_sync_command_after_adjustments, shell=True, capture_output=True, text=True)
    print("Output from wallet sync command after fee adjustments:")
    print(result_sync_after_adjustments.stdout)

    # Wait for 60 seconds to allow changes to take effect
    time.sleep(60)

def run_node_commands(start, end, image_directory, env_directory, file_prefix, file_extension):
    for i in range(start, end + 1):
        # Construct the file name
        file_number = str(i).zfill(5)
        image_path = os.path.join(image_directory, f"{file_prefix}{file_number}.{file_extension}")

        # Check if file exists
        if not os.path.isfile(image_path):
            print(f"File not found: {image_path}")
            continue

        # Extract base file name without serial number
        base_file_name = os.path.basename(image_path).split('.')[0][:-5]

        # Construct and run the first command
        mint_command = f"node . mint <D9pqzxiiUke5eodEzMmxZAxpFcbvwuM4Hg-But Your Address for Recieving> {image_path}"
        result_mint = subprocess.run(mint_command, shell=True, capture_output=True, text=True)
        print("Output from mint command:")
        print(result_mint.stdout)

        # Check if there is an error in the first command
        if result_mint.stderr:
            print("Error in mint command:")
            print(result_mint.stderr)

        # Check for specific error message in the first command's output
        if "'64: too-long-mempool-chain'" in result_mint.stdout:
            print("Detected specific error message, proceeding to wallet sync...")

        # Wait for the initial delay after mint command
        time.sleep(BASE_RETRY_DELAY_SECONDS)

        # Loop for the second command
        retry_count = 0
        while retry_count < MAX_RETRIES:
            wallet_sync_command = "node . wallet sync"
            result_sync = subprocess.run(wallet_sync_command, shell=True, capture_output=True, text=True)
            print("Output from wallet sync command:")
            print(result_sync.stdout)

            if result_sync.stderr:
                print("Error in wallet sync command:")
                print(result_sync.stderr)

            # Check for success message
            if "inscription txid:" in result_sync.stdout:
                print("Successful inscription, extracting txid and updating JSON file.")
                txid = re.search(r"inscription txid: (\w+)", result_sync.stdout).group(1)
                update_json_file(base_file_name, image_path, txid)
                break

            # Check for the specific error and retry
            elif "'64: too-long-mempool-chain'" in result_sync.stdout:
                mempool_congestion = get_mempool_congestion()
                dynamic_delay = calculate_dynamic_delay_and_adjust_fees(mempool_congestion, env_directory)
                print(f"Detected specific error message, retrying in {dynamic_delay} seconds...")
                time.sleep(dynamic_delay)
                retry_count += 1
            else:
                print("Unknown response, stopping the retry loop.")
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

# Replace with file extension
file_extension = 'jpg'
# Enter the range of files to inscribe.
start = 1
end = 21
run_node_commands(start, end, image_directory, env_directory, file_prefix, file_extension)
