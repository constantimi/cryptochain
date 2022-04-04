# Generated by Django 2.2.6 on 2019-10-27 19:43

import api.models
import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received_time', models.BigIntegerField(auto_created=True, blank=True, null=True)),
                ('height', models.BigIntegerField(auto_created=True, blank=True, null=True)),
                ('block_index', models.BigIntegerField(auto_created=True, blank=True, null=True)),
                ('size', models.BigIntegerField(auto_created=True, blank=True, null=True)),
                ('n_tx', models.BigIntegerField(auto_created=True, blank=True, null=True)),
                ('title', models.CharField(max_length=255, null=True)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2019, 10, 27, 19, 43, 36, 801607, tzinfo=utc), null=True)),
                ('currency', models.CharField(max_length=255, null=True)),
                ('hash', models.CharField(blank=True, default=api.models.create_hash, max_length=255, null=True)),
                ('previous_block', models.CharField(blank=True, max_length=255, null=True)),
                ('merkle_root', models.CharField(blank=True, max_length=255, null=True)),
                ('time', models.DateTimeField(default=datetime.datetime(2019, 10, 27, 19, 43, 36, 801708, tzinfo=utc))),
                ('nonce', models.CharField(blank=True, max_length=255, null=True)),
                ('difficulty', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gas_price', models.BigIntegerField(auto_created=True, blank=True, null=True)),
                ('gas', models.BigIntegerField(auto_created=True, blank=True, null=True)),
                ('value', models.CharField(auto_created=True, blank=True, max_length=255, null=True)),
                ('tx_index', models.BigIntegerField(auto_created=True, blank=True, null=True)),
                ('block_number', models.BigIntegerField(auto_created=True, blank=True, null=True)),
                ('nonce', models.CharField(auto_created=True, blank=True, max_length=255, null=True)),
                ('fee', models.BigIntegerField(auto_created=True, blank=True, null=True)),
                ('title', models.CharField(max_length=255, null=True)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2019, 10, 27, 19, 43, 36, 802235, tzinfo=utc), null=True)),
                ('currency', models.CharField(max_length=255, null=True)),
                ('hash', models.TextField(blank=True, default=api.models.create_hash, max_length=255, null=True)),
                ('block_hash', models.TextField(blank=True, max_length=255, null=True)),
                ('time', models.DateTimeField(default=datetime.datetime(2019, 10, 27, 19, 43, 36, 802349, tzinfo=utc))),
                ('belonging_to', models.TextField(blank=True, max_length=255, null=True)),
                ('relayed_by', models.TextField(blank=True, max_length=255, null=True)),
                ('inputs', models.TextField(blank=True, max_length=255, null=True)),
                ('outputs', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_output', models.BigIntegerField(auto_created=True, blank=True, null=True)),
                ('value', models.BigIntegerField(blank=True, max_length=255, null=True)),
                ('tx_hash', models.TextField(blank=True, max_length=255, null=True)),
                ('transaction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_input', models.BigIntegerField(auto_created=True, blank=True, null=True)),
                ('address', models.TextField(blank=True, max_length=255, null=True)),
                ('tx_hash', models.TextField(blank=True, max_length=255, null=True)),
                ('transaction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Transaction')),
            ],
        ),
    ]
