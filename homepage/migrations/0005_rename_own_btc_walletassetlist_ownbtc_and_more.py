# Generated by Django 4.0.3 on 2022-04-24 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_delete_walletassetbalance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='walletassetlist',
            old_name='own_btc',
            new_name='ownbtc',
        ),
        migrations.RenameField(
            model_name='walletassetlist',
            old_name='own_usdt',
            new_name='ownusdt',
        ),
    ]