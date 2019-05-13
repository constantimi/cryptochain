import os

from blockchain.models import Block, Transaction
from blockchain_parser.blockchain import Blockchain
from django.utils import timezone


def gather_bitcoin_data():
    """Instantiate the Blockchain by giving the path to the directory"""
    """containing the .blk files created by bitcoind"""

    inc = 0
    count = 0

    print('the script started ...')
    blockchain = Blockchain(os.path.expanduser('~/.bitcoin/blocks'))

    """Adds blocks and transaction into Database"""
    index = 0
    for block in blockchain.get_unordered_blocks():

        new_block = Block(
            fee=0,
            nonce='',
            n_tx=block.n_transactions,
            size=block.size,
            block_index=index,
            height=block.height,
            received_time=timezone.localtime(timezone.now()),
            id=index,
            title="Block " + str(index),
            date_posted=timezone.localtime(timezone.now()),
            hash=block.hash,
            previous_block=block.header,
            merkle_root=blockchain.__hash__(),
            time=timezone.localtime(timezone.now())
        )

        new_block.save()
        print(count, "Record Block{} inserted successfully into blockchain_block table".format(index))
        count += 1

        block_number = 0
        for transaction in block.transactions:
            new_transaction = Transaction(
                nonce='', block_number=block_number,
                tx_index=transaction.txid,
                time=transaction.locktime,
                value=0,
                gas=0,
                gas_price=0,
                id=inc,
                title="Transaction " + str(inc),
                date_posted=timezone.localtime(timezone.now()),
                hash=transaction.hash,
                block_hash=block.hash,
                belonging_to='',
                relayed_by='',
                inputs=transaction.inputs
            )
            new_transaction.save()
            print(count, "Record Transaction{} inserted successfully into blockchain_transaction table".format(inc))

            inc += 1
            count += 1
            block_number += 1


if __name__ == '__main__':
    gather_bitcoin_data()
