# Generated by Django 4.0.4 on 2022-06-09 13:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('homepage', '0001_initial'), ('homepage', '0002_walletassetlist_time'), ('homepage', '0003_walletassetbalance'), ('homepage', '0004_delete_walletassetbalance'), ('homepage', '0005_rename_own_btc_walletassetlist_ownbtc_and_more'), ('homepage', '0006_walletassetbalance'), ('homepage', '0007_rename_usdtblance_walletassetbalance_usdtbalance'), ('homepage', '0008_alter_walletassetbalance_time'), ('homepage', '0009_remove_wallet_savings_balance_and_more'), ('homepage', '0010_cryptobotsettings'), ('homepage', '0011_alter_coinlist_price_alter_coinlist_totalasks_and_more'), ('homepage', '0012_alter_coinlist_price_alter_coinlist_totalasks_and_more'), ('homepage', '0013_alter_coinlist_price_alter_coinlist_totalasks_and_more'), ('homepage', '0014_coinlist_close_coinlist_high_coinlist_low_and_more'), ('homepage', '0015_coinlist_numtrades_coinlist_takerbasevol_and_more'), ('homepage', '0016_ohlcv_remove_coinlist_close_remove_coinlist_high_and_more'), ('homepage', '0017_remove_ohlcv_slug')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BinanceSymbolList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='CoinList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('coin', models.CharField(max_length=15)),
                ('price', models.DecimalField(decimal_places=18, max_digits=36, null=True)),
                ('totalbids', models.DecimalField(decimal_places=18, max_digits=36, null=True)),
                ('totalasks', models.DecimalField(decimal_places=18, max_digits=36, null=True)),
                ('slug', models.SlugField(max_length=15, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset', models.CharField(max_length=15)),
                ('spot_balance', models.DecimalField(decimal_places=18, default=0.0, max_digits=36)),
            ],
        ),
        migrations.CreateModel(
            name='WalletAssetList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset', models.CharField(max_length=15)),
                ('free', models.DecimalField(decimal_places=18, default=0.0, max_digits=36)),
                ('locked', models.DecimalField(decimal_places=18, default=0.0, max_digits=36)),
                ('ownusdt', models.DecimalField(decimal_places=8, default=0.0, max_digits=19)),
                ('ownbtc', models.DecimalField(decimal_places=8, default=0.0, max_digits=19)),
                ('time', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WalletAssetBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('usdtbalance', models.DecimalField(decimal_places=8, default=0.0, max_digits=19)),
                ('btcbalance', models.DecimalField(decimal_places=8, default=0.0, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='CryptoBotSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(max_length=100)),
                ('api_secret', models.CharField(max_length=100)),
                ('SECRET_KEY', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ohlcv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin', models.CharField(max_length=15)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('open', models.DecimalField(decimal_places=18, max_digits=36, null=True)),
                ('high', models.DecimalField(decimal_places=18, max_digits=36, null=True)),
                ('low', models.DecimalField(decimal_places=18, max_digits=36, null=True)),
                ('close', models.DecimalField(decimal_places=18, max_digits=36, null=True)),
                ('volume', models.DecimalField(decimal_places=18, max_digits=36, null=True)),
                ('numtrades', models.DecimalField(decimal_places=18, max_digits=36, null=True)),
                ('takerbasevol', models.DecimalField(decimal_places=18, max_digits=36, null=True)),
                ('takerquotevol', models.DecimalField(decimal_places=18, max_digits=36, null=True)),
            ],
        ),
    ]
