"""
Minimal NEO node with custom code in a background thread.

It will log events from all smart contracts on the blockchain
as they are seen in the received blocks.
"""
import threading

from logzero import logger
from neo.Core.Blockchain import Blockchain
from neo.Implementations.Blockchains.LevelDB.LevelDBBlockchain import LevelDBBlockchain
from neo.Network.NodeLeader import NodeLeader
from neo.Settings import settings
from twisted.internet import reactor, task
# from blockchain.models import Block, Transaction


def send_data():
    for i in range(10):
        block = Blockchain.Default().GetBlockByHeight(i)
        print('Block Index: {}\nSize: {}\nTransactions: {}\nHash: {}\n'
              'PrevHash: {}\nMerkleRoot: {}\nRawData: {}\nHeader: {}\n'.
              format(block.Index,
                     block.Size(),
                     block.Transactions,
                     block.Hash,
                     block.PrevHash,
                     block.MerkleRoot,
                     block.RawData,
                     block.Header
                     ))
        for transaction in block.Transactions:
            print('Transaction Hash: {}'.format(transaction.Hash))

        logger.info("Block %s / %s", str(Blockchain.Default().Height),
                    str(Blockchain.Default().HeaderHeight))

        # new_block = Block(
        #     fee=0.00087,
        #     nonce=block.nonce,
        #     n_tx=len(block.transactions),
        #     size=block.size,
        #     block_index=block.number,
        #     height=block.difficulty,
        #     received_time=block.timestamp,
        #     id=index,
        #     title="Block " + str(index),
        #     date_posted=timezone.localtime(timezone.now()),
        #     hash=block.hash,
        #     previous_block=block.receiptsRoot,
        #     merkle_root=block.parentHash,
        #     time=timezone.localtime(timezone.now())
        # )
        #
        # new_block.save()

        # new_transaction = Transaction(
        #       nonce='', block_number=block_number,
        #       tx_index=transaction.txid,
        #       time=transaction.locktime,
        #       value=0,
        #       gas=0,
        #       gas_price=0,
        #       id=inc,
        #       title="Transaction " + str(inc),
        #       date_posted=timezone.localtime(timezone.now()),
        #       hash=transaction.hash,
        #       block_hash=block.hash,
        #       belonging_to='',
        #       relayed_by='',
        #       inputs=transaction.inputs
        #   )
        # new_transaction.save()
        # print(count, "Record Transaction{} inserted successfully into blockchain_transaction table".format(inc))
        #


def gather_neo_data():
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
    d = threading.Thread(name='daemon_send_data', target=send_data)
    d.setDaemon(True)  # daemonizing the thread will kill it when the main thread is quit
    d.start()

    """Run all the things (blocking call)"""
    reactor.run()
    logger.info("Shutting down.")


if __name__ == '__main__':
    gather_neo_data()
