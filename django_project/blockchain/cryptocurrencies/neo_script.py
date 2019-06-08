"""
Minimal NEO node with custom code in a background thread.

It will log events from all smart contracts on the blockchain
as they are seen in the received blocks.
"""
import threading

from blockchain.models import Block, Transaction, Input
from django.utils import timezone
from logzero import logger
from neo.Core.Blockchain import Blockchain
from neo.Implementations.Blockchains.LevelDB.LevelDBBlockchain import LevelDBBlockchain
from neo.Network.NodeLeader import NodeLeader
from neo.Settings import settings
from twisted.internet import reactor, task

"""Blocks count created in DB"""
blocks_count = 2


def send_data(block_index, tx_index, input_index, ouput_index):
    """Adds blocks and transaction into Database"""
    tx_number = tx_index
    input_number = input_index
    block_number = block_index

    count = 0

    for index in range(blocks_count):
        block = Blockchain.Default().GetBlockByHeight(index)

        """Add block to Block model"""
        new_block = Block(
            nonce=None,
            difficulty=None,
            currency="NEO",
            n_tx=len(block.Transactions),
            size=block.Size(),
            block_index=block_number,
            height=None,
            received_time=block.Header.Timestamp,
            id=block_number,
            title="Block " + str(block_number),
            date_posted=timezone.localtime(timezone.now()),
            hash=block.Hash,
            previous_block=block.PrevHash,
            merkle_root=block.MerkleRoot,
            time=timezone.localtime(timezone.now())
        )

        new_block.save()

        print(count, "Record NEO Block {} inserted successfully into blockchain_block table".format(block_number))

        count += 1

        """Logger Block info"""
        logger.info("Block %s / %s", str(Blockchain.Default().Height),
                    str(Blockchain.Default().HeaderHeight))

        tx_inx = 0
        for transaction in block.Transactions:

            new_transaction = Transaction(
                fee=0,
                currency="NEO",
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
                hash=transaction.Hash,
                block_hash=block.Hash,
                belonging_to=None,
                relayed_by=None,
                inputs=transaction.getAllInputs(),
                outputs=None
            )

            new_transaction.save()

            print(count,
                  "Record NEO Transaction {} inserted successfully into blockchain_transaction table".format(tx_number))

            tx_number += 1
            count += 1
            tx_inx += 1

            for input in transaction.getAllInputs():
                new_input = Input(
                    id=input_number,
                    id_input=input_number,
                    transaction=new_transaction,
                    address=input.transaction_hash,
                    tx_hash=transaction.Hash
                )

                new_input.save()

                print(count, "Record NEO Input {} inserted successfully into blockchain_input table".format(input_number))

                input_number += 1
                count += 1

        block_number += 1


def gather_neo_data(block_index, tx_index, input_index, ouput_index):
    """Is connected with Database"""
    print('the script started ...')

    """Use MainNet"""
    settings.setup_mainnet()

    """Setup the Blockchain"""
    blockchain = LevelDBBlockchain(settings.chain_leveldb_path)
    Blockchain.RegisterBlockchain(blockchain)
    dbloop = task.LoopingCall(Blockchain.Default().PersistBlocks)
    dbloop.start(.1)
    NodeLeader.Instance().Start()

    """Start a thread with custom code"""
    d = threading.Thread(name='daemon_send_data', target=send_data, args=(block_index, tx_index, input_index, ouput_index))
    d.setDaemon(True)  # daemonizing the thread will kill it when the main thread is quit
    d.start()

    """Run all the things (blocking call)"""
    reactor.run()
    logger.info("Shutting down.")

