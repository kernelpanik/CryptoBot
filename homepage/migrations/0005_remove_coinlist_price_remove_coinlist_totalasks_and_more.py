# Generated by Django 4.0.5 on 2022-06-24 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_remove_coinlist_id_remove_walletassetbalance_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coinlist',
            name='price',
        ),
        migrations.RemoveField(
            model_name='coinlist',
            name='totalasks',
        ),
        migrations.RemoveField(
            model_name='coinlist',
            name='totalbids',
        ),
    ]
