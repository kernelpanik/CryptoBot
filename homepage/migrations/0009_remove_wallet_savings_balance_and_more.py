# Generated by Django 4.0.4 on 2022-04-28 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_alter_walletassetbalance_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='savings_balance',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='staking_balance',
        ),
    ]