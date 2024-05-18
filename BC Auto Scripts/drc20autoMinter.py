import subprocess
import time
import os
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# Setup environment variables and RPC connection
rpc_user = os.getenv('RPC_USER', 'your_rpc_user')
rpc_password = os.getenv('RPC_PASSWORD', 'password')
rpc_host = os.getenv('RPC_HOST', 'localhost')
rpc_port = os.getenv('RPC_PORT', '22555')
address = os.getenv('DOGECOIN_ADDRESS', 'DCHxodkzaKCLjmnG4LP8uH6NKynmntmCNz')
batch_size = int(os.getenv('BATCH_SIZE', '12'))
total_batches = int(os.getenv('TOTAL_BATCHES', '100'))
token = os.getenv('TOKEN_NAME', 'onyx')
amount = int(os.getenv('TOKEN_AMOUNT', '1000'))
rpc_connection = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}/")

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

def batch_process(batch_size, number_of_batches, address, token, amount):
    """Processes multiple batches of Node.js mint commands."""
    command_template = f"node . drc-20 mint {address} {token} {amount}"

    for batch_number in range(1, number_of_batches + 1):
        print(f"Starting batch {batch_number}/{number_of_batches} with {batch_size} mints.")
        last_txid = None
        for i in range(batch_size):
            output = run_node_command(command_template)
            if output:
                txid = extract_txid(output)
                if txid:
                    last_txid = txid
        if last_txid and wait_for_tx_confirmation(last_txid):
            print(f"Batch {batch_number} completed and confirmed.")
        else:
            print(f"Batch {batch_number} did not complete successfully.")

def main():
    # Process all batches
    batch_process(batch_size, total_batches, address, token, amount)

if __name__ == "__main__":
    main()
