# v4 README

## Overview:

This version (v4) of the Python script enhances the inscription automation process for a collection of digital images using Node.js commands. Specifically, it addresses and resolves errors related to 25KB file-sized inscriptions. The script interacts with a blockchain-based system, performing minting and wallet synchronization for each image within a specified range.

## Prerequisites:

Node.js installed.

Proper configuration of the Node.js environment.

Access to the collection directory containing images for inscription.

JSON file to store transaction IDs and corresponding image details.

Dogecoin address for inscribing images.

## Usage:

Replace doge_address with the actual Dogecoin address for inscribing images.

Set the correct directory, file_prefix, and file_extension values for your image collection.

Specify the range of files to be inscribed by setting start and end.

Run the script to automate the inscription process.

## Script Workflow:
### Minting Command:


Constructs file names based on the specified range.

Executes the minting command using Node.js, capturing the output.

Checks for success or specific errors in the minting process.

## Successful Mint Handling:

If the minting is successful, updates the JSON file with the transaction ID.

Waits for 100 seconds before moving to the next image.

## Wallet Synchronization:

In case of specific errors, proceeds to wallet sync.

Executes the wallet sync command to confirm inscription.

Retries in case of specific errors, with a wait time of 100 seconds between retries.

Updates a JSON file with transaction IDs for successful inscriptions.

## Important Notes:

Ensure Node.js is correctly configured and accessible in the system.

Backup important files before running the script.

Monitor the script execution for any errors or warnings.

# Example:

## Dogecoin address to inscribe to.
doge_address = 'DCHxodkzaKCLjmnG4LP8uH6NKynmntmCNz'

## Replace with dir to collection.
directory = 'C:\\doginals-main\\RiceCerts\\serializers' #C:\doginals-main\RiceCerts\serializers

## Replace with collection name. The file name without the serial number.
file_prefix = 'smallCert_c'

## Replace with file extension.
file_extension = 'png'

## Enter the range of files to inscribe.
start = 327
end = 337
run_node_commands(start, end, directory, file_prefix, file_extension)

### Note: Customize the script parameters according to your Dogecoin address, collection, and image file details.
