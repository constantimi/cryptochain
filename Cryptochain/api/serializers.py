from rest_framework import serializers

from .models import Block, Transaction, Input, Output

"""BLOCKS SERIALIZER"""


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = (
            'title',
            'hash',
            'currency',
            'previous_block',
            'merkle_root',
            'time',
            'nonce',
            'difficulty',
            'n_tx',
            'size',
            'block_index',
            'height',
            'received_time'
        )

    def create(self, validated_data):
        return Block.objects.create(**validated_data)


"""TRANSACTION SERIALIZER"""


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            'fee',
            'currency',
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
            'inputs',
            'outputs'
        )

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)


"""INPUT SERIALIZER"""


class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input
        fields = (
            'id_input',
            'transaction',
            'address',
            'tx_hash'
        )

    def create(self, validated_data):
        return Input.objects.create(**validated_data)


"""OUTPUT SERIALIZER"""


class OutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Output
        fields = (
            'id_output',
            'transaction',
            'value',
            'tx_hash'
        )

    def create(self, validated_data):
        return Output.objects.create(**validated_data)