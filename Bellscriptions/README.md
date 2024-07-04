# Bellscriptions

A minter and protocol for inscriptions on Bells. 

## ⚠️⚠️⚠️ Important ⚠️⚠️⚠️
Use this wallet for inscribing only! Always inscribe from this wallet to a different address, e.g. one you created with Ordinals Wallet. 
This wallet is not meant for storing funds or inscriptions.

## Prerequisites

This guide requires a bit of coding knowledge and running Ubuntu on your local machine or a rented one. To use this, you'll need to use your terminal to setup a Bellscoin node, clone this repo and install Node.js on your computer.

### Setup Bellscoin node

#### Get Nintondo Core Wallet

On your Terminal, type the following commands:

```
cd
wget https://github.com/Nintondo/bellscoin/releases/download/2.0.0/bells-2.0.0-x86_64-linux-gnu.tar.gz
tar -xvzf bells-2.0.0-x86_64-linux-gnu.tar.gz
```
#### Run Bellscoin node
```
cd bells-2.0.0
cd bin
./bellsd -daemon
```
#### Configure node
Create a `bells.conf` file with your node information:
```
cd
cd ~/.bells
touch bells.conf
vi bells.conf
```
Copy and Paste the following into the `bells.conf` file
```
rpcuser=z4ch
rpcpassword=zord
rpcport=19918
server=1
listen=1
```

Wait for the node to fully sync.
Check the status by typing the command `bells-cli getinfo` on the same directory.

### Install NodeJS

Please head over to (https://github.com/nodesource/distributions#using-ubuntu) and follow the installation instructions.

Check if they are installed by running the following commands:
`node -v` and `npm -v`
![image](https://github.com/zachzwei/Doginals_z4ch/assets/35627271/8cf77d41-46b8-47af-a0ae-dff566059f58)


### Setup Bellscriptions

#### Clone Bellscription minter
On your Terminal, type the following commands:
```
cd
git clone https://github.com/ordinals-wallet/bellscriptions.git
```
#### Setup minter

Install dependencies:

```
cd bellscriptions
npm install
```

Create a `.env` file with your node information:

On your Terminal, type the following commands:
```
touch .env
vi .env
```
Copy and Paste the following into the `.env` file
```
NODE_RPC_URL=http://127.0.0.1:19918
NODE_RPC_USER=z4ch
NODE_RPC_PASS=zord
TESTNET=false
FEE_PER_KB=3300030
```

## Funding

Generate a new `.wallet.json` file:

```
node . wallet new
```

Then send BELLS to the address displayed. Once sent, sync your wallet:

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

Repeating:

```
node . mint <address> <path> <repeat>
```

Examples:

```
node . mint BQQcsCCBiQn1aJsrrNzTg4Lm7MMd1PzZHq dog.jpeg
```

```
node . mint BQQcsCCBiQn1aJsrrNzTg4Lm7MMd1PzZHq mint.json 100
```

## Bellmap

You may bulk mint bellmap by specifying an address to receive and a start and end bellmap number

```
node . mint-bellmap <address> <start> <end>
```

Examples:

```
node . mint-bellmap BQQcsCCBiQn1aJsrrNzTg4Lm7MMd1PzZHq 0 100
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

The bellscriptions protocol allows any size data to be inscribed onto subwoofers.

An inscription is defined as a series of push datas:

```
"ord"
OP_1
"text/plain; charset=utf8"
OP_0
"Woof!"
```

For bellscriptions, we introduce a couple extensions. First, content may spread across multiple parts:

```
"ord"
OP_2
"text/plain; charset=utf8"
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
"text/plain; charset=utf8"
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

There's a problem with the node connection. Your `bellscoin.conf` file should look something like:

```
rpcuser=z4ch
rpcpassword=zord
rpcport=19918
server=1
```

Make sure `port` is not set to the same number as `rpcport`. Also make sure `rpcauth` is not set.

Your `.env file` should look like:

```
NODE_RPC_URL=http://127.0.0.1:19918
NODE_RPC_USER=ape
NODE_RPC_PASS=zord
TESTNET=false
```

### I'm getting "insufficient priority" errors when minting

The miner fee is too low. You can increase it up by putting FEE_PER_KB=300000000 in your .env file or just wait it out. The default is 100000000 but spikes up when demand is high.
