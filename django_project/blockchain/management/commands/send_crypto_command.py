from blockchain.cryptocurrencies.bitcoin_script import gather_bitcoin_data
from blockchain.cryptocurrencies.ethereum_script import gather_ethereum_data
from blockchain.cryptocurrencies.neo_script import gather_neo_data
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        data1 = gather_bitcoin_data(0, 0, 0, 0)

        data2 = gather_ethereum_data(data1[0], data1[1], data1[2], data1[3])

        gather_neo_data(data2[0], data2[1], data2[2], data2[3])
