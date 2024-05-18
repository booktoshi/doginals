import subprocess
import time
import json
import os
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# Setup environment variables and RPC connection
rpc_user = os.getenv('RPC_USER', 'your_rpc_user')
rpc_password = os.getenv('RPC_PASSWORD', 'your_rpc_password')
rpc_host = os.getenv('RPC_HOST', 'localhost')
rpc_port = os.getenv('RPC_PORT', '22555')
batch_size = int(os.getenv('BATCH_SIZE', '12'))
total_batches = int(os.getenv('TOTAL_BATCHES', '100'))
token = os.getenv('TOKEN_NAME', 'onyx')
amount = int(os.getenv('TOKEN_AMOUNT', '1000'))
rpc_connection = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}/")

def read_airdrop_list():
    """Reads the airdrop list from a JSON file."""
    with open('airDropList.json', 'r') as file:
        data = json.load(file)
    return data.get('airDropList', [])

def update_progress_log(index, address):
    """Updates the progress log JSON file with the last processed address index."""
    with open('progressLog.json', 'w') as file:
        json.dump({'last_index': index, 'address': address}, file)

def read_progress_log():
    """Reads the last processed index from the progress log JSON file."""
    if not os.path.exists('progressLog.json'):
        return 0  # Start from the beginning if log does not exist
    with open('progressLog.json', 'r') as file:
        data = json.load(file)
    return data.get('last_index', 0)

def run_node_command(command):
    """Execute a Node.js command and return the output."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print("Error executing command:", result.stderr)
    except Exception as e:
        print(f"An error occurred executing command: {e}")
    return None

def extract_txid(output):
    """Extracts the TXID from the command output."""
    if "inscription txid:" in output:
        return output.split()[-1]
    return None

def wait_for_tx_confirmation(txid):
    """Waits for a transaction to be confirmed."""
    print(f"Waiting for confirmation of TXID: {txid}")
    retries = 300  # 300 retries * 10 seconds = 50 minutes max wait
    while retries > 0:
        try:
            tx_info = rpc_connection.gettransaction(txid)
            if tx_info and tx_info.get("confirmations", 0) >= 1:
                print(f"Transaction {txid} is confirmed.")
                return True
        except JSONRPCException as e:
            print(f"RPC Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(10)  # Wait for 10 seconds before retrying
        retries -= 1
    print(f"Failed to confirm transaction {txid} after multiple retries.")
    return False

def batch_process(address_list):
    """Processes batches of Node.js mint commands based on the provided address list."""
    start_index = read_progress_log()
    for i in range(start_index, len(address_list), batch_size):
        last_txid = None
        for j in range(batch_size):
            if i + j >= len(address_list):
                break
            address = address_list[i + j]['address']
            command = f"node . drc-20 mint {address} {token} {amount}"
            print(f"Processing {command} (index {i + j})")
            output = run_node_command(command)
            if output:
                txid = extract_txid(output)
                if txid:
                    last_txid = txid
                    update_progress_log(i + j, address)  # Update progress log as soon as TXID is extracted
        if last_txid and wait_for_tx_confirmation(last_txid):
            print(f"Batch {i // batch_size + 1} completed and confirmed.")
        else:
            print(f"Batch {i // batch_size + 1} did not complete successfully.")
        time.sleep(1)  # Optional delay between transactions

def main():
    address_list = read_airdrop_list()
    batch_process(address_list)

if __name__ == "__main__":
    main()
