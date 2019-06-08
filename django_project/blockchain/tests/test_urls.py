from django.urls import reverse, resolve
from django.test import SimpleTestCase


class TestUrls(SimpleTestCase):

    def test_home_url(self):
        path = reverse('blockchain-home', kwargs={})
        assert resolve(path).view_name == 'blockchain-home'

    def test_about_url(self):
        path = reverse('blockchain-about', kwargs={})
        assert resolve(path).view_name == 'blockchain-about'

    def test_blocks_url(self):
        path = reverse('blockchain-blocks', kwargs={})
        assert resolve(path).view_name == 'blockchain-blocks'

    def test_block_int_url(self):
        path = reverse('blockchain-block-details', kwargs={'pk': 1})
        assert resolve(path).view_name == 'blockchain-block-details'

    def test_transactions_url(self):
        path = reverse('blockchain-transactions', kwargs={})
        assert resolve(path).view_name == 'blockchain-transactions'

    def test_transaction_int_url(self):
        path = reverse('blockchain-transaction-details', kwargs={'pk': 1})
        assert resolve(path).view_name == 'blockchain-transaction-details'

    def test_input_url(self):
        path = reverse('blockchain-inputs', kwargs={})
        assert resolve(path).view_name == 'blockchain-inputs'

    def test_input_int_url(self):
        path = reverse('blockchain-input-details', kwargs={'pk': 1})
        assert resolve(path).view_name == 'blockchain-input-details'

    def test_output_url(self):
        path = reverse('blockchain-outputs', kwargs={})
        assert resolve(path).view_name == 'blockchain-outputs'

    def test_output_int_url(self):
        path = reverse('blockchain-output-details', kwargs={'pk': 1})
        assert resolve(path).view_name == 'blockchain-output-details'
