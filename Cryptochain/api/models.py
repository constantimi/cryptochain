import hashlib
import time

from django.db import models
from django.urls import reverse
from django.utils import timezone

"""Default method for generating hash"""


def create_hash():
    """This function generate 10 character long hash"""
    h = hashlib.sha1()
    h.update(str(time.time()).encode('utf-8'))
    return h.hexdigest()[:-10]


class Block(models.Model):
    """a block from blockchain"""
    title = models.CharField(max_length=255, null=True)
    date_posted = models.DateTimeField(default=timezone.localtime(timezone.now()), null=True, editable=True)
    currency = models.CharField(max_length=255, null=True)
    hash = models.CharField(max_length=255, default=create_hash, null=True, blank=True)
    previous_block = models.CharField(max_length=255, null=True, blank=True)
    merkle_root = models.CharField(blank=True, null=True, max_length=255)
    time = models.DateTimeField(default=timezone.localtime(timezone.now()), editable=True)
    nonce = models.CharField(max_length=255, null=True, blank=True)
    difficulty = models.CharField(max_length=255, null=True, blank=True)
    n_tx = models.BigIntegerField(auto_created=True, null=True, blank=True)
    size = models.BigIntegerField(auto_created=True, null=True, blank=True)
    block_index = models.BigIntegerField(auto_created=True, null=True, blank=True)
    height = models.BigIntegerField(auto_created=True, null=True, blank=True)
    received_time = models.BigIntegerField(auto_created=True, null=True, blank=True)

    @property
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blockchain-block-details', kwargs={'pk': self.pk})

    def flush(self):
        pass


class Transaction(models.Model):
    """a transaction from blockchain"""
    title = models.CharField(max_length=255, null=True)
    date_posted = models.DateTimeField(default=timezone.localtime(timezone.now()), null=True, editable=True)
    fee = models.BigIntegerField(auto_created=True, null=True, blank=True)
    currency = models.CharField(max_length=255, null=True)
    hash = models.TextField(max_length=255, default=create_hash, null=True, blank=True)
    nonce = models.CharField(max_length=255, auto_created=True, null=True, blank=True)
    block_hash = models.TextField(max_length=255, null=True, blank=True)
    block_number = models.BigIntegerField(auto_created=True, null=True, blank=True)
    tx_index = models.BigIntegerField(auto_created=True, null=True, blank=True)
    time = models.DateTimeField(default=timezone.localtime(timezone.now()), editable=True)
    belonging_to = models.TextField(blank=True, null=True, max_length=255)
    relayed_by = models.TextField(blank=True, null=True, max_length=255)
    value = models.CharField(max_length=255, auto_created=True, null=True, blank=True)
    gas = models.BigIntegerField(auto_created=True, blank=True, null=True)
    gas_price = models.BigIntegerField(auto_created=True, blank=True, null=True)
    inputs = models.TextField(max_length=255, null=True, blank=True)
    outputs = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blockchain-transaction-details', kwargs={'pk': self.pk})

    def flush(self):
        pass


class Input(models.Model):
    id_input = models.BigIntegerField(auto_created=True, blank=True, null=True)
    transaction = models.ForeignKey(Transaction, blank=True, null=True, on_delete=models.CASCADE)
    address = models.TextField(blank=True, max_length=255, null=True)
    tx_hash = models.TextField(blank=True, max_length=255, null=True)

    def get_absolute_url(self):
        return reverse('blockchain-input-details', kwargs={'pk': self.pk})

    def flush(self):
        pass


class Output(models.Model):
    id_output = models.BigIntegerField(auto_created=True, blank=True, null=True)
    transaction = models.ForeignKey(Transaction, blank=True, null=True, on_delete=models.CASCADE)
    value = models.BigIntegerField(blank=True, max_length=255, null=True)
    tx_hash = models.TextField(blank=True, max_length=255, null=True)

    def get_absolute_url(self):
        return reverse('blockchain-output-details', kwargs={'pk': self.pk})

    def flush(self):
        pass
