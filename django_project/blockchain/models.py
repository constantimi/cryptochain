import hashlib
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from django.utils import timezone
import time


# Default method for generating hash


def create_hash():
    """This function generate 10 character long hash"""
    h = hashlib.sha1()
    h.update(str(time.time()).encode('utf-8'))
    return h.hexdigest()[:-10]


# One-Many User -> Blocks

class Block(models.Model):
    title = models.CharField(max_length=255, null=True)
    date_posted = models.DateTimeField(default=timezone.now, null=True, editable=False)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # block content
    hash = models.CharField(max_length=255, default=create_hash, null=True, blank=True)
    previous_block = models.CharField(max_length=255, null=True, blank=True)
    merkle_root = models.CharField(blank=True, null=True, max_length=255)
    time = models.DateTimeField(default=timezone.now, editable=True)
    fee = models.BigIntegerField(auto_created=True, null=True, blank=True)
    nonce = models.CharField(max_length=255, auto_created=True, null=True, blank=True)
    n_tx = models.BigIntegerField(auto_created=True, null=True, blank=True)
    size = models.BigIntegerField(auto_created=True, null=True, blank=True)
    block_index = models.BigIntegerField(auto_created=True, null=True, blank=True)
    height = models.BigIntegerField(auto_created=True, null=True, blank=True)
    received_time = models.BigIntegerField(auto_created=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blockchain-block-details', kwargs={'pk': self.pk})

    def flush(self):
        pass


class Transaction(models.Model):
    title = models.CharField(max_length=255, null=True)
    date_posted = models.DateTimeField(default=timezone.now, null=True, editable=False)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # transaction content
    hash = models.TextField(max_length=255, default=create_hash, null=True, blank=True)
    nonce = models.CharField(max_length=255, auto_created=True, null=True, blank=True)
    block_hash = models.TextField(max_length=255, null=True, blank=True)
    block_number = models.BigIntegerField(auto_created=True, blank=True)
    tx_index = models.BigIntegerField(auto_created=True, blank=True)
    time = models.DateTimeField(default=timezone.now,editable=False)
    belonging_to = models.TextField(blank=True, max_length=255)
    relayed_by = models.TextField(blank=True, max_length=255)
    value = models.BigIntegerField(auto_created=True, blank=True)
    gas = models.BigIntegerField(auto_created=True, blank=True)
    gas_price = models.BigIntegerField(auto_created=True, blank=True)
    inputs = models.TextField(max_length=255, null=True, blank=True)


class Input(models.Model):
    transaction = models.ForeignKey(Transaction, blank=True, null=True, on_delete=models.CASCADE)

    n = models.IntegerField(auto_created=True, blank=True)
    value = models.IntegerField(auto_created=True, blank=True)
    address = models.TextField(blank=True, max_length=255)
    tx_index = models.IntegerField(auto_created=True, blank=True)
    type = models.IntegerField(auto_created=True, blank=True)
    script = models.TextField(blank=True, max_length=255)
    script_sig = models.TextField(blank=True, max_length=255)
    sequence = models.IntegerField(auto_created=True, blank=True)


class Output(models.Model):
    transaction = models.ForeignKey(Transaction, blank=True, null=True, on_delete=models.CASCADE)
    n = models.IntegerField(auto_created=True, blank=True)
    value = models.IntegerField(auto_created=True, blank=True)
    address = models.TextField(blank=True, max_length=255)
    tx_index = models.IntegerField(auto_created=True, blank=True)
    script = models.TextField(blank=True, max_length=255)
    spent = models.BooleanField(default=False)
