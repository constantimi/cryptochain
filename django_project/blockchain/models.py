import hashlib
import time

from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from django.utils import timezone

# Default method for generating hash


def create_hash():
    """This function generate 10 character long hash"""
    h = hashlib.sha1()
    h.update(str(time.time()).encode('utf-8'))
    return h.hexdigest()[:-10]


# One-Many User -> Blocks

class Block(models.Model):
    title = models.CharField(max_length=255)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # block content
    hash = models.CharField(max_length=255, default=create_hash, unique=True, null=True, blank=True)
    previous_block = models.CharField(max_length=255, null=True, blank=True)
    merkle_root = models.CharField(blank=True, null=True, max_length=255)
    time = models.IntegerField(auto_created=True, null=True, blank=True)
    bits = models.IntegerField(auto_created=True, null=True, blank=True)
    fee = models.IntegerField(auto_created=True, null=True, blank=True)
    nonce = models.IntegerField(auto_created=True, null=True, blank=True)
    n_tx = models.IntegerField(auto_created=True, null=True, blank=True)
    size = models.IntegerField(auto_created=True, null=True, blank=True)
    block_index = models.IntegerField(auto_created=True, null=True, blank=True)
    height = models.IntegerField(auto_created=True, null=True, blank=True)
    received_time = models.IntegerField(auto_created=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blockchain-block-details', kwargs={'pk': self.pk})

    def flush(self):
        pass


class Transaction(models.Model):
    title = models.CharField(max_length=255, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # transaction content
    double_spend = models.BooleanField()
    block_height = models.IntegerField(auto_created=True, blank=True)
    time = models.IntegerField(auto_created=True, blank=True)
    relayed_by = models.TextField(blank=True, max_length=255)
    hash = models.TextField(blank=True, max_length=255)
    tx_index = models.IntegerField(auto_created=True, blank=True)
    version = models.IntegerField(auto_created=True, blank=True)
    size = models.IntegerField(auto_created=True, blank=True)
    inputs = ArrayField(models.CharField(max_length=200))
    outputs = ArrayField(models.CharField(max_length=200))


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
