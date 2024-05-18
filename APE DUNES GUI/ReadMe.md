# Dunes GUI EXE

## Overview

The Dunes GUI is a simplified interface for managing Dunes Protocol operations conveniently through a graphical user interface (GUI).
With this application, users can generate wallets, sync wallets, send funds, deploy Dunes, mint Dunes, print balances, and perform various other Dunes-related tasks, with no coding experience.
Just need a Active Node and some Dogecoin!

## Features

Generate and sync wallets

Send and receive funds

Deploy and mint Dunes

Print Dune balances

Simplified interface for easy navigation

## Requirements

Create Working Directory: The GUI exe should be saved in a file path you Create:
 
`C:\Dunes-GUI`

Along with blank `.wallet.json` file and a copy of the Dunes acceptable  `.env` file that should be all you need.

If you already have dunes and doginals client set up, and and are in filepath named `C:\ Doginals-main\Dunes-main` it will recognize current wallet info particularly in that path and it adds your current dunes minting wallet info from your `.wallet.json`, this is for people already minting both. For everyone not set up and just running a node and wallet funded with doge you can add your `.wallet.json` key and address in the GUI, and a created directory.

Active Dunes Node: Before using the Dunes GUI, ensure that you have an active Dunes node running on your system. 
The GUI interacts with the Dunes Protocol through this node.

**Dogecoin**: The Dunes Protocol is built on top of Dogecoin, so make sure you have a basic understanding of Dogecoin and its functionalities.

*Note: It does make commands through operating system dealing with the node.js and dunes and doginals scripts. Because of that dependency it flags microsoft defender, so I noticed when I dowloaded file from Github, it got flagged so I had to adjust the windows defender bypass setting to let it through.*

## Usage
**Download the Executable: Download the executable file (dunes_gui.exe for Windows) from the provided source.**

Launch the Application: Double-click the dunes_gui.exe file to launch the Dunes GUI application.

Navigate the Interface: Use the buttons provided in the interface to perform various Dunes-related tasks. 
Each button corresponds to a specific operation such as generating wallets, sending funds, or printing balances.

Follow On-Screen Instructions: Depending on the task you wish to perform, the application may prompt you for additional information such as addresses, amounts, or other parameters. 
Follow the on-screen instructions to complete the tasks.

View Outputs: After executing a task, the application will display relevant outputs or messages in pop-up dialog boxes. 
Review these outputs to ensure that your operations were successful.

Close the Application: Once you've completed your tasks, you can close the application by clicking the close button (X) in the top-right corner of the window.

# Button Functions:

***Details:***

**Click File button to set `.env` file for fees, you can change every setting but its recommended to leave the env file as follows:**

PROTOCOL_IDENTIFIER=D

NODE_RPC_URL=http://127.0.0.1:22555

NODE_RPC_USER=rpc_user

NODE_RPC_PASS=rpc_password

TESTNET=false

FEE_PER_KB=100000000

UNSPENT_API=https://unspent.dogeord.io/api/v1/address/unspent/

ORD=https://ord.dunesprotocol.com/


**`.wallet.json` should look like this:**

{

  "privkey": "",

  "address": "",

  "utxos": []

}

**Generate Wallet:**

Creates a New wallet in your Dogecoin node

**Sync Wallet:**

Syncs wallet and prints Dogecoin balance

**Existing Wallet**

-Existing Wallet: If you have been followiing me and already have file paths based on our repos for C:\Doginals-main\Dunes-main it will scan for this wallet.json in this directory first, if you have that file it will copy it to C:\Dunes-GUI then it syncs. 
If you dont have this path already it scans GUI path to see if you have a exsisting wallet inside the exe since the time you used it last then syncs. 
If no wallet it prompts you to create a new one in which you have to record the Private Key and Address manually, or enter private key, in which you can enter the private key you just created or already have to use.

-Generate Wallet:

Creates a New wallet in your Dogecoin node

-Enter Private Key:
 
You can enter the key and address for the wallet you would like to use.


**Print Safe UTXOs:** 

Command to print UTXOs in your wallet that are safe to spend.

**Split Wallet:**

This allows you to split up your UTXOs, enter the amount you want to split into when prompted

**Send Funds:**

 Send Dogecoin to another wallet

**Deploy Dune:**

To Deploy a dune:

When Prompted Enter Your Dune name in all caps and other required data: 

GOODNIGHT•WEB3 <blocks> <limit-per-mint> <timestamp-deadline> <decimals> <symbol> <mint-self> <is-open>

-Example for a dune that can be minted for 100 blocks, with a limit of 100000000, a deadline of 0, 8 decimals, symbol R (emojis also work 🔥 💰 🚀 in example DOGE•COIN•DUNES 100 100000000 0 8 🚀 true true  or TO•THE•MOON 100 100000000 0 8 R true true   both will work). 
First true value means 1R is minted during deploy. 
Second true means mints are open.


examples:

TRY•EVEN•HARDER 100 100000000 0 8 R true true

TRY•EVEN•HARDER 100 100000000 0 8 🔥 true true


**Mint Dune:** 

Input data when instructed

<id> <amount> <to>

Example:

5132520/31 100000000 D9UcJkdirVLY11UtF77WnC8peg6xRYsogu

**Mass Mint Dunes:**

Input data when instructed <id> <amount> <number-of-mints> <to>

Example:

5132520/31 100000000 10 D9UcJkdirVLY11UtF77WnC8peg6xRYsogu

**Print Dune Balance:**

Check the Dunes in your wallet

**Split Send Dunes:**

Split dunes from one output to many:

<txhash> <vout> <dune> <decimals> <amounts> <addresses>

Example: 

 15a0d646c03e52c3bf66d67c910caa9aa30e40ecf27f495f1b9c307a4ac09c2e 1 WHO•LET•THE•DUNES•OUT 8 2,3 DDjbkNTHPZAq3f6pzApDzP712V1xqSE2Ya,DTnBdk1evnpbKe1qeCoeATHZnAVtwNR2xe

**Send or Combine Dunes:**

Combine dunes from multiple outputs to one or Send Dunes from this wallet to another: 

<address> <utxo-amount> <dune>

Example: 

D9UcJkdirVLY11UtF77WnC8peg6xRYsogu 1 GET•DUNE•STONED

***Each button command has an associated action that performs the specified wallet operation.
These are the main commands defined in the Dunes script. If you have specific questions about any of these commands or if you need assistance with a particular aspect of the GUI, feel free to ask!***

## Support

For any issues, questions, or feedback, please feel free to reach out. I'm here to help!

# Contributing

If you'd like to contribute or donate to our projects, please donate in Dogecoin. For contributors its as easy as opening issues, and creating pull requests

If You would like to support with Donations, Send all Dogecoin tothe following Contributors:

"handle": ***"Great Ape"*** "at": ***"@Greatape42069E"*** **"Dogecoin_address": "D9pqzxiiUke5eodEzMmxZAxpFcbvwuM4Hg"**

## License

This project is licensed under the MIT License.

![image](https://github.com/GreatApe42069/dunes-gui/assets/153969184/660b391f-df98-4977-b1e3-7b7655ad48c6)



![image](https://github.com/GreatApe42069/dunes-gui/assets/153969184/a9b433e3-0b35-4b01-8310-dac6bdd86987)
