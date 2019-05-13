from blockchain.cryptocurrencies.neo_script import gather_neo_data
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        gather_neo_data()
