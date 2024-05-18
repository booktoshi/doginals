# Doginals Congested Mempool Bulk Auto Mint Script

This script automates the process of minting and inscribing Dogecoin NFTs for your collection.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contribution](#contribution)
- [License](#license)

## Overview

This `Doginals_Congested_Mempool_Bulk-Auto-mint-Script` simplifies the minting and inscribing process for Dogecoin Doginal inscription images. It handles the submission of minting transactions and monitors the Dogecoin Core wallet for successful inscriptions. This script also, calls Real-time updates on mempool congestion using Dogechain's WebSocket API, and utilizes a built in customizable Dynamic retry mechanism to handle mempool congestion.

## Features

- Automated minting and inscription of Dogecoin Doginal NFTs.
- Real-time updates on mempool congestion using Dogechain's WebSocket API.
- Dynamic retry mechanism to handle mempool congestion.
- Easy configuration for collection-specific details.

## Requirements

- Dogecoin Core Wallet installed and synchronized.
- Node.js installed (for running the script).
- Python installed (for additional functionality).
- Ensure you have the websocket-client library installed.


## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/GreatApe42069/Doginals_Congested_Mempool_Bulk-Auto-mint-Script.git
cd Doginals_Congested_Mempool_Bulk-Auto-mint-Script
```


2. Install the required Node.js packages:

`npm install`

3. (Optional) Install any additional Python packages:

- `pip install -r requirements.txt`
- `pip install charset-normalizer`
- `pip install requests`

4. Ensure you have the `websocket-client` library installed:

`pip install websocket-client`

5. Navigate to the directory where YOUR Python scripts are located using the cd command:

`cd C:\Doginals-main`

6. Run the commands mentioned earlier:

`pip install charset-normalizer`

`pip install requests`


## Usage:

To use the Doginal Inscription Script, follow these steps:

1. Configure the script by updating the necessary parameters in the script (e.g., wallet address, file paths).

2. Run this script with the specified range of files to inscribe:

`node auto_inscriber_v3.py`

3. Monitor the console output for the script's progress and any error messages.


## Configuration
Before running the script, make sure to configure the following parameters in the script or through environment variables:

- `MEMPOOL_WS_URL`: Real-time WebSocket URL providing mempool congestion information. Update this parameter with the WebSocket URL you want to use.

You can also customize the script's behavior by modifying the following parameters in the script:

`MAX_RETRIES`: Maximum number of retries for inscription in case of failure.

`BASE_RETRY_DELAY_SECONDS`: Initial delay between retries (in seconds).

The parameter (congestion / 1000) is used to scale down the congestion value obtained from the Dogechain WebSocket API. The original congestion value might be in a larger range, and dividing it by 1000 is a normalization step to make it more suitable for adjusting the delay.

In the `calculate_dynamic_delay function`, the line `BASE_RETRY_DELAY_SECONDS`  (congestion / 1000) is calculating a dynamic delay based on the congestion value. This adjusted delay is then compared with the `BASE_RETRY_DELAY_SECONDS`, ensuring that it doesn't go below a certain threshold.

You can experiment with this scaling factor based on your observations and requirements. If the congestion values received from the Dogechain WebSocket API are in a different range, you may adjust the scaling accordingly. The goal is to have a reasonable delay that reflects the current network congestion.
Update these parameters according to your requirements.

## Contribution:
Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or create a pull request.

## License:
This project is licensed under the MIT License.
