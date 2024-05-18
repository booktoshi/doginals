# Dogecoin Auto_Inscription_Airdrop Script

## Description:

-This Python script automates the process of inscribing and airdroppng images. 

-It extracts Dogecoin addresses from a specified JSON file, mints inscriptions from specified filepath, airdrops the minted inscription, and updates a JSON file with transaction details. 

-The script handles specific error messages and ensures successful inscription.

# Features:

## Blockchain Integration: 

Interacts with the Dogecoin blockchain for minting inscriptions.

Error Handling: Detects and addresses specific error messages during the minting process.

JSON File Update: Updates a JSON file with transaction details for each successfully minted image.


# Usage

##Install Dependencies:

Ensure you have Node.js installed, as the script utilizes Node.js commands. 

Additionally, install Python dependencies:

`pip install -r requirements.txt`


## Configure JSON File:

Edit the airDropList.json file to include Dogecoin addresses in the format:

{
  "airDropList": [
    {"dogecoin_address": "ADDRESS1"},
    {"dogecoin_address": "ADDRESS2"},
    ...
  ]
}

## Run the Script:

Replace the placeholder details in the script with your specific information:

## Replace with your specific details

directory = 'C:\\doginals-main\\RiceCerts'
file_prefix = 'animated'
file_extension = 'webp'
start = 337
end = 351

## Execute the script:

`python auto_inscription_script.py`

# Configuration:

*file_name:*

JSON file containing Dogecoin addresses (airDropList.json by default).

*directory:*
 
Directory containing images to be inscribed.

*file_prefix:*

Prefix for image filenames.

*file_extension:*

 Extension of the image files.

*start:*

 Starting index for image filenames.

*end:*

Ending index for image filenames.

## Implementation

-The script is implemented in Python and utilizes Node.js for interacting with the Dogecoin blockchain. It extracts addresses from the JSON file, mints and sends inscriptions, handles errors, and updates a JSON file with transaction details.

Feel free to reach out if you encounter any issues or have questions!