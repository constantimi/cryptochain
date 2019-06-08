from blockchain.cryptocurrencies.ethereum_script import gather_ethereum_data
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        gather_ethereum_data(0, 0, 0, 0)
