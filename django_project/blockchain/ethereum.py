from web3.auto.infura import w3
from web3 import Web3

w3.eth.getBlock('latest')

print(w3.isConnected())
print(w3.eth.blockNumber)

# web3.py instance
w3 = Web3(Web3.EthereumTesterProvider())


block = w3.eth.getBlock('latest')
# AttributeDict({
#   'hash': '0xe8ad537a261e6fff80d551d8d087ee0f2202da9b09b64d172a5f45e818eb472a',
#   'number': 4022281,
#   # ... etc ...
# })

print(block['number'])
# block.number
# block.number = 4022282

"""Contrancts"""
# https://web3py.readthedocs.io/en/stable/contracts.html

"""Automatic provider detection"""
# https://web3py.readthedocs.io/en/stable/providers.html

"""Transactions"""
# https://web3py.readthedocs.io/en/stable/web3.eth.html
