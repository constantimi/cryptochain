## Cryptochain

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

### Explanation
A blockchain, originally block chain, is a growing list of records, called blocks, which are linked using cryptography. ... It is "an open, distributed ledger that can record transactions between two parties efficiently and in a verifiable and permanent way".
<br/>

### About the project?
Cryptochain is an opensource platform for deep explanation in the crypro technologies.

## Neo

Read more in the [documentation on ReadTheDocs](https://neo-python.readthedocs.io/en/latest/).
<br/>

 - What does it currently do

    * This project aims to be a full port of the original C# NEO project
    * Run a Python based P2P node

- What will it do

- Getting started

* Please follow directions in the install section
<br/>
The main functionality for this project is contained within the cli application np-prompt. You can view usage details here

```
    neo-python-rpc: NEO RPC client in Python
    neo-boa: Write smart contracts with Python
```


* Sister projects

    - [neo-python-rpc](https://github.com/CityOfZion/neo-python-rpc): NEO RPC client in Python
    - [neo-boa](https://github.com/CityOfZion/neo-boa): Write smart contracts with Python


## Bitcoin

Read more in the [documentation on ReadTheDocs](https://github.com/alecalve/python-bitcoin-blockchain-parser). [View the whitepaper](https://bitcoin.org/bitcoin.pdf).
<br/>
This Python 3 library provides a parser for the raw data stored by bitcoind. 

### Features
- Detects outputs types
- Detects addresses in outputs
- Interprets scripts
- Supports SegWit
- Supports ordered block parsing

### Examples

Below are two basic examples for parsing the blockchain. More examples are available in the examples directory.

### Unordered Blocks

This blockchain parser parses raw blocks saved in Bitcoin Core's `.blk` file format. Bitcoin Core does not guarantee that these blocks are saved in order. If your application does not require that blocks are parsed in order, the `Blockchain.get_unordered_blocks(...)` method can be used:

```python
import os 
from blockchain_parser.blockchain import Blockchain

# Instantiate the Blockchain by giving the path to the directory 
# containing the .blk files created by bitcoind
blockchain = Blockchain(os.path.expanduser('~/.bitcoin/blocks'))
for block in blockchain.get_unordered_blocks():
    for tx in block.transactions:
        for no, output in enumerate(tx.outputs):
            print("tx=%s outputno=%d type=%s value=%s" % (tx.hash, no, output.type, output.value))
```

### Ordered Blocks

If maintaining block order is necessary for your application, you should use the `Blockchain.get_ordered_blocks(...)` method. This method uses Bitcoin Core's LevelDB index to locate ordered block data in it's `.blk` files.

```python
import os 
from blockchain_parser.blockchain import Blockchain

# To get the blocks ordered by height, you need to provide the path of the
# `index` directory (LevelDB index) being maintained by bitcoind. It contains
# .ldb files and is present inside the `blocks` directory.
for block in blockchain.get_ordered_blocks(os.path.expanduser('~/.bitcoin/blocks/index'), end=1000):
    print("height=%d block=%s" % (block.height, block.hash))
```

Blocks can be iterated in reverse by specifying a start parameter that is greater than the end parameter.

```python
for block in blockchain.get_ordered_blocks(os.path.expanduser('~/.bitcoin/blocks/index'), start=510000, end=0):
    print("height=%d block=%s" % (block.height, block.hash))
```

Building the LevelDB index can take a while which can make iterative development and debugging challenging. For this reason, `Blockchain.get_ordered_blocks(...)` supports caching the LevelDB index database using [pickle](https://docs.python.org/3.6/library/pickle.html). To use a cache simply pass `cache=filename` to the ordered blocks method. If the cached file does not exist it will be created for faster parsing the next time the method is run. If the cached file already exists it will be used instead of re-parsing the LevelDB database. 

```python
for block in blockchain.get_ordered_blocks(os.path.expanduser('~/.bitcoin/blocks/index'), cache='index-cache.pickle'):
    print("height=%d block=%s" % (block.height, block.hash))
```

## Ehtereum 

A Python implementation of [web3.js](https://github.com/ethereum/web3.js)

<br/>
**Web3.py** is a python library for interacting with Ethereum. Its API is derived from the Web3.js Javascript API and should be familiar to anyone who has used **web3.js**.
<br/>

* Python 3.6+ support
<br/>
 Read more in the [documentation on ReadTheDocs](http://web3py.readthedocs.io/). [View the change log on Github](docs/releases.rst).
<br/>

![text altr](https://commercecopilot.com/wp-content/uploads/2019/04/Logo-Design.jpg)
