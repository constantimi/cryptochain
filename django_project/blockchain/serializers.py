from rest_framework import serializers

from blockchain.models import Block


# serializers for a block
class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = (
                  'title',
                  'hash',
                  'prevous_block',
                  'merkle_root',
                  'time',
                  'bits',
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
        instance.bits = validated_data.get('bits', instance.bits)
        instance.fee = validated_data.get('fee', instance.fee)
        instance.nonce = validated_data.get('nonce', instance.nonce)
        instance.n_tx = validated_data.get('n_tx', instance.n_tx)
        instance.size = validated_data.get('size', instance.size)
        instance.block_index = validated_data.get('block_index', instance.block_index)
        instance.height = validated_data.get('height', instance.height)
        instance.received_time = validated_data.get('received_time', instance.received_time)
