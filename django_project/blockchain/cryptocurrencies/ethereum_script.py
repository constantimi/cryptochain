from blockchain.models import Block, Transaction, Input
from django.utils import timezone
from web3.auto.infura import w3


def gather_ethereum_data(block_index, tx_index, input_index, output_index):
    """Is connected with Database"""

    print("the script started ...")
    print("is connected: " + str(w3.isConnected()))
    print(timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M:%S'))

    """Adds blocks and transaction into Database"""
    block_number = block_index
    tx_number = tx_index
    input_number = input_index
    output_number = output_index

    count = 0

    """Blocks count created in DB"""
    blocks_count = 2

    for index in range(blocks_count):
        """Take new block from web3 ethereum"""
        block = w3.eth.getBlock(w3.eth.blockNumber - index)

        """Add block to Block model"""

        new_block = Block(
            nonce=block.nonce.hex(),
            difficulty=block.difficulty,
            currency="ETH",
            n_tx=len(block.transactions),
            size=block.size,
            block_index=block_number,
            height=block.difficulty,
            received_time=block.timestamp,
            id=block_number,
            title="Block " + str(block_number),
            date_posted=timezone.localtime(timezone.now()),
            hash=block.hash.hex(),
            previous_block=block.receiptsRoot.hex(),
            merkle_root=block.parentHash.hex(),
            time=timezone.localtime(timezone.now())
        )

        new_block.save()
        print(count, "Record ETH Block {} inserted successfully into blockchain_block table".format(block_number))

        count += 1

        """Take new transaction form web3 ethereum"""
        li = block.transactions
        for index in range(len(li)):

            transaction = w3.eth.getTransaction(li[index])

            try:
                f = transaction.gas * transaction.gasPrice
            except ValueError as e:
                f = 0            
            
            try:
                n = transaction.nonce
            except ValueError as e:
                n = 0 

            try:
                v = transaction.value
            except ValueError as e:
                v = 0

            new_transaction = Transaction(
                fee= f,
                currency="ETH",
                nonce=n,
                block_number=block_number,
                tx_index=index,
                time=timezone.localtime(timezone.now()),
                value=v,
                gas=transaction.gas,
                gas_price=transaction.gasPrice,
                id=tx_number,
                title="Transaction " + str(tx_number),
                date_posted=timezone.localtime(timezone.now()),
                hash=transaction.hash.hex(),
                block_hash=transaction.blockHash.hex(),
                belonging_to=transaction['from'],
                relayed_by=transaction.to,
                inputs=transaction['input'],
                outputs=None

            )

            new_transaction.save()
            print(count,
                  "Record ETH Transaction {} inserted successfully into blockchain_transaction table".format(tx_number))

            tx_number += 1
            count += 1

            new_input = Input(
                id=input_number,
                id_input=input_number,
                transaction=new_transaction,
                address=transaction['input'],
                tx_hash=transaction.hash.hex()
            )
            new_input.save()

            print(count, "Record ETH Input {} inserted successfully into blockchain_input table".format(input_number))

            input_number += 1
            count += 1

            """Ethereum's transaction doesn't have outputs"""

        block_number += 1

    data = [block_number, tx_number, input_number, output_number]

    return data
