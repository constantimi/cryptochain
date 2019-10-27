import os

from api.models import Block, Transaction, Input, Output
from blockchain_parser.blockchain import Blockchain
from bit.network import fees
from django.utils import timezone


def gather_bitcoin_data(block_index, tx_index, input_index, output_index):
    """Instantiate the Blockchain by giving the path to the directory"""
    """containing the .blk files created by bitcoind"""

    tx_number = tx_index
    input_number = input_index
    output_number = output_index
    block_number = block_index

    count = 0

    print('the script started ...')
    print(timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M:%S'))
    blockchain = Blockchain(os.path.expanduser('~/.bitcoin/blocks'))

    """Blocks count created in DB"""
    block_count = 2

    """Adds blocks and transaction into Database"""

    for block in blockchain.get_unordered_blocks():

        if block_count <= 0:
            break

        new_block = Block(
            nonce=block.header.nonce,
            difficulty=block.header.difficulty,
            currency="BTC",
            n_tx=block.n_transactions,
            size=block.size,
            block_index=block_number,
            height=block.height,
            received_time=None,
            id=block_number,
            title="Block " + str(block_number),
            date_posted=timezone.localtime(timezone.now()),
            hash=block.hash,
            previous_block=block.header.previous_block_hash,
            merkle_root=block.header.merkle_root,
            time=timezone.localtime(timezone.now())

        )

        new_block.save()

        print(count, "Record BTC Block {} inserted successfully into blockchain_block table".format(block_number))

        count += 1

        tx_inx = 0
        for transaction in block.transactions:
            new_transaction = Transaction(
                fee=fees.get_fee(),
                currency="BTC",
                nonce=None,
                block_number=block_number,
                tx_index=tx_inx,
                time=timezone.localtime(timezone.now()),
                value=None,
                gas=0,
                gas_price=0,
                id=tx_number,
                title="Transaction " + str(tx_number),
                date_posted=timezone.localtime(timezone.now()),
                hash=transaction.hash,
                block_hash=block.hash,
                belonging_to=None,
                relayed_by=None,
                inputs=transaction.inputs,
                outputs=transaction.outputs
            )

            new_transaction.save()

            print(count,
                  "Record BTC Transaction {} inserted successfully into blockchain_transaction table".format(tx_number))

            tx_number += 1
            count += 1
            tx_inx += 1

            for input in transaction.inputs:
                new_input = Input(
                    id=input_number,
                    id_input=input_number,
                    transaction=new_transaction,
                    address=input.transaction_hash,
                    tx_hash=transaction.hash,

                )
                new_input.save()

                print(count,
                      "Record BTC Input {} inserted successfully into blockchain_input table".format(input_number))

                input_number += 1
                count += 1

                for output in transaction.outputs:
                    
                    new_output = Output(
                        id=output_number,
                        id_output=output_number,
                        transaction=new_transaction,
                        value=output.value,
                        tx_hash=transaction.hash
                    )
                    new_output.save()

                    print(count,
                          "Record BTC Output {} inserted successfully into blockchain_output table".format(
                              output_number))
                    output_number += 1
                    count += 1

        block_number += 1

        block_count -= 1

    data = [block_number, tx_number, input_number, output_number]

    return data
