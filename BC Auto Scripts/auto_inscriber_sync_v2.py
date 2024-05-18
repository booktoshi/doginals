import subprocess
import time
import re

def run_node_sync():
    while True:
        wallet_sync_command = "node . wallet sync"
        result_sync = subprocess.run(wallet_sync_command, shell=True, capture_output=True, text=True)
        print("Output from wallet sync command:")
        print(result_sync.stdout)

        if result_sync.stderr:
            print("Error in wallet sync command:")
            print(result_sync.stderr)

        # Check for success message
        txid_search = re.search("inscription txid: (\w+)", result_sync.stdout)
        if txid_search:
            txid = txid_search.group(1)
            print(f"Successful inscription, TXID: {txid}")
            break

        # Sleep for 100 seconds before retrying
        print("Retrying in 100 seconds...")
        time.sleep(100)

run_node_sync()
