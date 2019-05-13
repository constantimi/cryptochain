from rest_framework import serializers
from .models import Block, Transaction


"""BLOCKS SERIALIZER"""


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = (
                  'title',
                  'hash',
                  'previous_block',
                  'merkle_root',
                  'time',
                  'fee',
                  'nonce',
                  'n_tx',
                  'size',
                  'block_index',
                  'height',
                  'received_time'
                  )

    def create(self, validated_data):
        return Block.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.hash = validated_data.get('hash', instance.hash)
        instance.previous_block = validated_data.get('previous_block', instance.previous_block)
        instance.merkle_root = validated_data.get('merkle_root', instance.merkle_root)
        instance.time = validated_data.get('time', instance.time)
        instance.fee = validated_data.get('fee', instance.fee)
        instance.nonce = validated_data.get('nonce', instance.nonce)
        instance.n_tx = validated_data.get('n_tx', instance.n_tx)
        instance.size = validated_data.get('size', instance.size)
        instance.block_index = validated_data.get('block_index', instance.block_index)
        instance.height = validated_data.get('height', instance.height)
        instance.received_time = validated_data.get('received_time', instance.received_time)
        instance.save()
        return instance


"""TRANSACTION SERIALIZER"""


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
                  'nonce',
                  'block_number',
                  'tx_index',
                  'time',
                  'value',
                  'gas',
                  'gas_price',
                  'id',
                  'title',
                  'date_posted',
                  'hash',
                  'block_hash',
                  'belonging_to',
                  'relayed_by',
                  'inputs'
                  )

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nonce = validated_data.get('nonce', instance.nonce)
        instance.block_number = validated_data.get('block_number', instance.block_number)
        instance.tx_index = validated_data.get('tx_index', instance.tx_index)
        instance.time = validated_data.get('time', instance.time)
        instance.value = validated_data.get('value', instance.value)
        instance.gas = validated_data.get('gas', instance.gas)
        instance.gas_price = validated_data.get('gas_price', instance.gas_price)
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.date_posted = validated_data.get('date_posted', instance.date_posted)
        instance.hash = validated_data.get('hash', instance.hash)
        instance.block_hash = validated_data.get('block_hash', instance.block_hash)
        instance.belonging_to = validated_data.get('belonging_to', instance.belonging_to)
        instance.relayed_by = validated_data.get('relayed_by', instance.relayed_by)
        instance.inputs = validated_data.get('inputs', instance.inputs)
        instance.save()
        return instance




