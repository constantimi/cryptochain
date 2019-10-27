from api.cryptocurrencies.bitcoin_script import gather_bitcoin_data
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        gather_bitcoin_data(0, 0, 0, 0)
