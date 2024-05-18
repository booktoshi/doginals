# OG Auto inscriber Read Me

## Overview:

This Python script streamlines the automated inscription process for a collection of digital images using Node.js commands. It interacts with a blockchain-based system, performing minting and wallet synchronization for each image within a specified range.

## Prerequisites:

Node.js installed.

Proper configuration of the Node.js environment.

Access to the collection directory containing images for inscription.

JSON file to store transaction IDs and corresponding image details.

## Usage:

Replace <Your Doge Address for storing inscriptions Only> with the actual Dogecoin address in the mint_command.

Set the correct directory, file_prefix, and file_extension values for your image collection.

Specify the range of files to be inscribed by setting start and end.

Run the script to automate the inscription process.

# Script Workflow:
## Minting Command:

Constructs file names based on the specified range.

Executes the minting command using Node.js, capturing the output.

Handles errors and specific messages, proceeding to wallet sync if needed.

# Wallet Synchronization:

Executes the wallet sync command to confirm inscription.

Retries in case of specific errors, with a wait time of 60 seconds between retries.

Updates a JSON file with transaction IDs for successful inscriptions.

# Important Notes:

Ensure Node.js is correctly configured and accessible in the system.

Backup important files before running the script.

Monitor the script execution for any errors or warnings.

# Example:

## Replace with dir to collection.
directory = 'C:\\doginals-main\\collection'

## Replace with collection name. The file name without the serial number.
file_prefix = 'image'

## Replace with file extension.
file_extension = 'webp'

## Enter the range of files to inscribe.
start = 9
end = 20
run_node_commands(start, end, directory, file_prefix, file_extension)


### Note: Customize the script parameters according to your Dogecoin address, collection, and image file details.
