# Doginals

A minter and protocol for inscriptions on Dogecoin. 

## ⚠️⚠️⚠️ Important ⚠️⚠️⚠️

Use this wallet for inscribing only! Always inscribe from this wallet to a different address, e.g. one you created with Ordinals Wallet. This wallet is not meant for storing funds or inscriptions.

## Prerequisites

To use this, you'll need to use your console/terminal use Power Shell with Windows, install Node.js on your computer.

### Install NodeJS

Please head over to https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-22-04 and follow the installation instructions for Node.js

## Install Dogecoin Core for your Operating System https://bit.ly/dogecoinnode 
## Start your node for at least 1 minute

## Stop your node 

```
dogecoin-cli stop
```

## cd to your .dogecoin/ hidden folder in your system 

```
cd ~./.dogecoin/
```

## Update you dogecoin.conf file example.

```
nano dogecoin.conf
```

## Copy and paste below RPC settings

```
rpcuser=<username>
rpcpassword=<password>
rpcport=22555
rpcallowip=127.0.0.1
server=1
```

## Now save the files settings

```
ctrl + x ~~> Press Y ~~> ENTER
```

## Install Doginals

Download the repo by clicking <>code in the uper right of the GitHub and clicking Download ZIP                
Extract the root folder to your rooot dir.

Using the terimnal install. 
```
git clone https://github.com/booktoshi/doginals.git
cd doginals
npm install
``` 

After all dependencies are solved, you can configure the environment:

### Configure environment

`.env` and add your node information:

```
NODE_RPC_URL=http://127.0.0.1:22555
NODE_RPC_USER=<username>
NODE_RPC_PASS=<password>
TESTNET=false
FEE_PER_KB=30000000
```

You can get the current fee per kb from [here](https://mempool.jhoenicke.de/#DOGE,8h,weight).

### Using CLI

Import the private key to core ~/dogecoin-1.14.7/bin/ directory and you want to run the dogecoin-cli
run
./dogecoin-cli 
```
importprivkey <your_private_key> <optional_label> false
```
### Using QT
Settings>Options Wallets Enable coin controll.

Create a new wallet from shell.
```
node . wallet new
```
After creating your doginals wallet copy your private key from your doginals_folder/.wallet.

File>Import Private Key

Paste private key and name wallet.

Fund wallet.

## Funding

Then send DOGE to the address displayed. Once sent, sync your wallet:

```
node . wallet sync
```

If you are minting a lot, you can split up your UTXOs:

```
node . wallet split <count>
```

When you are done minting, send the funds back:

```
node . wallet send <address> <optional amount>
```

## Minting

From file:

```
node . mint <address> <path>
```

From data:

```
node . mint <address> <content type> <hex data>
```

Examples:

```
node . mint DSV12KPb8m5b6YtfmqY89K6YqvdVwMYDPn dog.jpeg
```

```
node . mint DSV12KPb8m5b6YtfmqY89K6YqvdVwMYDPn "text/plain;charset=utf-8" 576f6f6621 
```

**Note**: Please use a fresh wallet to mint to with nothing else in it until proper wallet for doginals support comes. You can get a paper wallet [here](https://www.fujicoin.org/wallet_generator?currency=Dogecoin).

## DRC-20

```
node . drc-20 mint <address> <ticker> <amount>
```

Examples: 

```
node . drc-20 mint D9pqzxiiUke5eodEzMmxZAxpFcbvwuM4Hg dogi 1000
```

## Viewing

Start the server:

```
node . server
```

And open your browser to:

```
http://localhost:3000/tx/15f3b73df7e5c072becb1d84191843ba080734805addfccb650929719080f62e
```

## Protocol

The doginals protocol allows any size data to be inscribed onto subwoofers.

An inscription is defined as a series of push datas:

```
"ord"
OP_1
"text/plain;charset=utf-8"
OP_0
"Woof!"
```

For doginals, we introduce a couple extensions. First, content may spread across multiple parts:

```
"ord"
OP_2
"text/plain;charset=utf-8"
OP_1
"Woof and "
OP_0
"woof woof!"
```

This content here would be concatenated as "Woof and woof woof!". This allows up to ~1500 bytes of data per transaction.

Second, P2SH is used to encode inscriptions.

There are no restrictions on what P2SH scripts may do as long as the redeem scripts start with inscription push datas.

And third, inscriptions are allowed to chain across transactions:

Transaction 1:

```
"ord"
OP_2
"text/plain;charset=utf-8"
OP_1
"Woof and "
```

Transaction 2

```
OP_0
"woof woof!"
```

With the restriction that each inscription part after the first must start with a number separator, and number separators must count down to 0.

This allows indexers to know how much data remains.

## FAQ

### I'm getting ECONNREFUSED errors when minting

There's a problem with the node connection. Your `dogecoin.conf` file should look something like:

```
rpcuser=ape
rpcpassword=zord
rpcport=22555
server=1
```

Make sure `port` is not set to the same number as `rpcport`. Also make sure `rpcauth` is not set.

Your `.env file` should look like:

```
NODE_RPC_URL=http://127.0.0.1:22555
NODE_RPC_USER=ape
NODE_RPC_PASS=zord
TESTNET=false
```

### I'm getting "insufficient priority" errors when minting

The miner fee is too low. You can increase it up by putting FEE_PER_KB=300000000 in your .env file or just wait it out. The default is 100000000 but spikes up when demand is high.

# Contributing

If you'd like to contribute or donate to our projects, please donate in Dogecoin. For contributors its as easy as opening issues, and creating pull requests


***If You would like to support with Donations, Send all Dogecoin tothe following Contributors:***

**"handle": "ApeZord" "at": "@Heimdall_Bull" "dogecoin_address": "DNmrp12LfsVwy2Q2B5bvpQ1HU7zCAczYob"**

**"handle": "Big Chief" "at": "@MartinSeeger2" "dogecoin_address": "DCHxodkzaKCLjmnG4LP8uH6NKynmntmCNz"**

**"handle": "Great Ape" "at": "@Greatape42069E" "dogecoin_address": "DBpLvNcR1Zj8B6dKJp4n3XEAT4FmRxbnJb"**

**"handle": "BillyBitcoins" "at": "@BillyBitcoins" "dogecoin_address": "DQAWs4LQKY3zVmorsLHDUCV7LE5ox6rho6"**

**"handle": "Booktoshi" "at": "@booktoshi" "dogecoin_address": "D9Ue4zayx5NP7sTSBMM9uwuzqpHv4HnkaN"**

**"handle": "ZachWei" "at": "@ZachZwei" "dogecoin_address": "DU3rJD4gAXEZkhnhp95idUfGssPD3bXBZa"**

**"handle": "Heimdall" "at": "@Heimdall_Bull" "dogecoin_address": "DEpFirPqu8DZUoCT7zEzGZs74JPTCF3ZMJ"**

## Contributors of Scripts and Programs Included:
  1.  https://github.com/apezord/doginals
  2.  https://github.com/GreatApe42069/dunes-gui
  3.  https://github.com/GreatApe42069/image-resize-compress-replace
  4.  https://github.com/martinseeger2002/dogcoin_ordinal_auto_inscriber
  5.  https://github.com/martinseeger2002/OW_API_SnapShot
  6.  https://github.com/H3imdall-dev/recurciveCollectionGen
  7.  https://github.com/sirduney/dunes-cli
  8.  https://github.com/zachzwei/bellscriptions

# License
This project is licensed under the MIT License.
