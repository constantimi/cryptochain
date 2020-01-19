import threading

from neo.Implementations.Blockchains.LevelDB.LevelDBBlockchain import LevelDBBlockchain
from neo.Core.Blockchain import Blockchain
from django.core.management.base import BaseCommand
from neo.Network.NodeLeader import NodeLeader
from twisted.internet import reactor, task
from logzero import logger
from neo.Settings import settings

# If you want the log messages to also be saved in a logfile, enable the
# next line. This configures a logfile with max 10 MB and 3 rotations:
# settings.set_logfile("/tmp/logfile.log", max_bytes=1e7, backup_count=3)


def custom_background_code():
    """ Custom code run in the background."""
    block = Blockchain.GenesisBlock()
    logger.info("Genesis Block:")
    logger.info("Header: %s", str(block.Header))
    logger.info("Hash: %s", str(block.Hash))
    logger.info("Merkle Root: %s", str(block.MerkleRoot))
    logger.info("PrevHash %s", str(block.PrevHash))
    logger.info("FullTransactions: %s", str(block.FullTransactions))


class Command(BaseCommand):
    def handle(self, *args, **options):

        '''Use TestNet'''
        settings.setup_testnet()

        '''Setup the blockchain'''
        blockchain = LevelDBBlockchain(settings.chain_leveldb_path)
        Blockchain.RegisterBlockchain(blockchain)

        dbloop = task.LoopingCall(Blockchain.Default())
        dbloop.start(.1)
        NodeLeader.Instance().Start()

        """Start a thread with custom code"""
        d = threading.Thread(name='demon_custom_background_code', target=custom_background_code, args=())
        d.setDaemon(True)  # daemonizing the thread will kill it when the main thread is quit
        d.start()

        """Run all the things (blocking call)"""
        reactor.run()
        logger.info("Shutting down.")

