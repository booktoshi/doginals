# OG2ReadMe

## Overview:

This Python script facilitates the automated inscription process for a collection of digital images using Node.js commands. It interacts with a blockchain-based system, performing minting and wallet synchronization for each image within a specified range.

## Prerequisites:

Node.js installed.

Proper configuration of the Node.js environment.

Access to the collection directory containing images for inscription.

JSON file to store transaction IDs and corresponding image details.

## Usage:

Replace <Your Inscription Receiving Address Here> with the actual receiving address in the mint_command.

Set the correct directory, file_prefix, and file_extension values for your image collection.

Specify the range of files to be inscribed by setting start and end.

Run the script to automate the inscription process.

# Script Workflow:
## Minting Command:


Constructs file names based on the specified range.

Executes the minting command using Node.js, capturing the output.

Handles errors and specific messages, proceeding to wallet sync if needed.

## Wallet Synchronization:

Executes the wallet sync command to confirm inscription.

Retries in case of specific errors, with a maximum retry count.

Updates a JSON file with transaction IDs for successful inscriptions.

## Important Notes:

Ensure Node.js is correctly configured and accessible in the system.

Backup important files before running the script.

Monitor the script execution for any errors or warnings.


## Example:

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

### Note: Ensure to customize the script parameters according to your collection and blockchain configuration.




