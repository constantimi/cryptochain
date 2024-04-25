## Cryptochain

Cryptochain is an opensource platform for deep explanation in the crypro technologies.

### Command Reference

The table below provides you with a quick reference of the necessary commands to start
your Django development process. You can find more detailed explanations in the reference table
for the "blockchain" app:

| Description                      | Command                                   |
|----------------------------------|-------------------------------------------|
| Set up a virtual environment     | python -m venv env                        |
| Activate the vir environment     | source env/bin/activate                   |
| Deactivate the vir environment   | deactivate                                |
| Install all dependecies          | python -m pip install -r requirements.txt |
| Pin your dependencies            | python -m pip freeze > requirements.txt   |
| Set up a Django project	       | django-admin startproject <projectname>   |
| Start the Django app	           | python manage.py startapp <appname>       |
| Run server on Django 	           | python manage.py runserver                |
| Test the Django app        	   | python manage.py test <appname>           |
| Migrate           	           | python manage.py migrate                  |


The following commands are for Postgres DB running on this app.
`sudo su - postgres`

To enter the postgres shell write:
`psql`


## Cryptonator

Read more in the [cryptonator](https://www.cryptonator.com/api)
Returns actual volume-weighted price, total 24h volume, rate change as well as prices and volumes across all connected exchanges.
Example request for BTC-USD

`
https://api.cryptonator.com/api/full/btc-usd
`

Sample JSON Response:

> {"ticker":{"base":"BTC","target":"USD","price":"443.7807865468","volume":"31720.1493969300","change":"0.3766203596","markets":[{"market":"bitfinex","price":"447.5000000000","volume":"10559.5293639000"},{"market":"bitstamp","price":"448.5400000000","volume":"11628.2880079300"},{"market":"btce","price":"432.8900000000","volume":"8561.0563600000"},{"market":"cryptotrade","price":"436.9999989900","volume":"0.3640623100"},{"market":"exmoney","price":"428.0000000000","volume":"7.9020328400"},{"market":"hitbtc","price":"442.6200000000","volume":"750.5900000000"},{"market":"justcoin","price":"453.4920000000","volume":"10.2583700000"},{"market":"kraken","price":"452.7042200000","volume":"17.7767076800"},{"market":"therocktrading","price":"440.0000000000","volume":"178.9300000000"},{"market":"vaultofsatoshi","price":"450.6428600000","volume":"5.3209840100"},{"market":"vircurex","price":"460.0000000000","volume":"0.1335082600"}]},"timestamp":1399490941,"success":true,"error":""}

**Params**

- Base - Base currency code
- Target - Target currency code
- Price - Volume-weighted price
- Volume - Total trade volume for the last 24 hours
- Change - Past hour price change
- Markets - Array with prices/volumes across all exchanges
    - Market - Name of the exchange
    - Price - Price on this exchange
    - Volume - 24h trade volume on this exchange
- Timestamp - Update time in Unix timestamp format
- Success - True or false
- Error - Error description


Replace btc-usd with the currency codes you need. Please refer to the actual list of supported currencies. Volume is displayed only for the cryptocurrencies that are actually traded on online exchanges. 

## Coindesk

Read more in the [coindesk](https://www.coindesk.com/coindesk-api) 
On the CoinDesk website, it is published the BPI in USD, EUR, and GBP, calculated every minute, based on criteria as discussed on the CoinDesk BPI page. This same data can be retrieved using the endpoint: 

`
https://api.coindesk.com/v1/bpi/currentprice.json
`

Sample JSON Response:

> {"time":{"updated":"Sep 18, 2013 17:27:00 UTC","updatedISO":"2013-09-18T17:27:00+00:00"},
"disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index. Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
"bpi":{"USD":{"code":"USD","symbol":"$","rate":"126.5235","description":"United States Dollar","rate_float":126.5235},
"GBP":{"code":"GBP","symbol":"£","rate":"79.2495","description":"British Pound Sterling","rate_float":79.2495},
"EUR":{"code":"EUR","symbol":"€","rate":"94.7398","description":"Euro","rate_float":94.7398}}}



## Coinmarketcap


Read more in the [coinmarketcap](https://coinmarketcap.com/api/documentation/v1)


The CoinMarketCap API is a suite of high-performance RESTful JSON endpoints that are specifically designed to meet the mission-critical demands of application developers, data scientists, and enterprise business platforms.



`
curl -H "X-CMC_PRO_API_KEY: b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c" -H "Accept: application/json" -d "id=1,1027" -G https://pro-api.coinmarketcap.com/v1/cryptocurrency/info
`

## Neo

Read more in the [documentation on ReadTheDocs.](https://neo-python.readthedocs.io/en/latest/)



#### What does it currently do

    * This project aims to be a full port of the original C# NEO project
    * Run a Python based P2P node

### What will it do


##### Please follow directions in the install section
    - The main functionality for this project is contained within the cli application [np-prompt](https://neo-python.readthedocs.io/en/latest/prompt.html)

##### Node with custom code

- Take a look at the examples here: [https://github.com/CityOfZion/neo-python/tree/development/examples](https://github.com/CityOfZion/neo-python/tree/development/examples)

##### Similar projects

- [neo-python-rpc](https://github.com/CityOfZion/neo-python-rpc): NEO RPC client in Python
- [neo-boa](https://github.com/CityOfZion/neo-boa): Write smart contracts with Python



## Bitcoin

Read more in the [documentation on ReadTheDocs.](https://github.com/alecalve/python-bitcoin-blockchain-parser)
[View the whitepaper.](https://bitcoin.org/bitcoin.pdf)


This Python 3 library provides a parser for the raw data stored by bitcoind. 

#### Features

   - Detects outputs types
   - Detects addresses in outputs
   - Interprets scripts
   - Supports SegWit
   - Supports ordered block parsing

#### Examples

Below are two basic examples for parsing the blockchain. More examples are available in the examples directory.

#### Unordered Blocks

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

#### Ordered Blocks

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

## Ethereum 

A Python implementation of 
[web3.js](https://web3js.readthedocs.io/en/v1.2.4/).



**Web3.py** is a python library for interacting with Ethereum. Its API is derived from the Web3.js Javascript API and should be familiar to anyone who has used **web3.js**.



* Python 3.6+ support

 Read more in the 
 [documentation on ReadTheDocs.](http://web3py.readthedocs.io/) 
 [View the change log on Github.](docs/releases.rst)


**web3.eth.defaultBlock**



The default block is used for certain methods. You can override it by passing in the defaultBlock as last parameter. The default value is “latest”.


`
web3.eth.getBalance()
`

`
web3.eth.getCode()
`

`
web3.eth.getTransactionCount()
`

`
web3.eth.getStorageAt()
`

`
web3.eth.call()
`

`
new web3.eth.Contract() -> myContract.methods.myMethod().call()
`

#### Property

Default block parameters can be one of the following:

Number: A block number 
`"genesis"` - String: The genesis block
`"latest"` - String: The latest block (current head of the blockchain)
`"pending"` - String: The currently mined block (including pending transactions)
Default is "latest"

#### Example

`
 $ web3.eth.defaultBlock;
 `

 > "latest"

 Set the default block

`
$ web3.eth.defaultBlock = 231;
`

### Repo Activity

![Alt](https://repobeats.axiom.co/api/embed/d7bf91e7e13197543ea980edbd1ba3e1aeb6b67e.svg "Repobeats analytics image")
