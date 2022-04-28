from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class CoinList(models.Model):
    date = models.DateTimeField(default=timezone.now)
    coin = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=36, decimal_places=18, default=0.0)
    totalbids = models.DecimalField(max_digits=36, decimal_places=18, default=0.0)
    totalasks = models.DecimalField(max_digits=36, decimal_places=18, default=0.0)
    slug = models.SlugField(max_length=15, unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.coin).upper()
        self.coin = (self.coin).upper()
        super(CoinList, self).save(*args, **kwargs)

    def __str__(self):
        return self.coin


class BinanceSymbolList(models.Model):
    symbol = models.CharField(max_length=15)

    def save(self, *args, **kwargs):
        #self.symbol = (self.symbol).upper()
        self.symbol = [elem.upper() for elem in (self.symbol) ]
        return super(BinanceSymbolList, self).save(*args, **kwargs)

    def __str__(self):
        return self.symbol





class Wallet(models.Model):
    asset =  models.CharField(max_length=15)
    spot_balance = models.DecimalField(max_digits=36, decimal_places=18, default=0.0)



    def __str__(self):
        return self.asset

class WalletAssetList(models.Model):
    time = models.TimeField(auto_now=True)
    asset =  models.CharField(max_length=15)
    free = models.DecimalField(max_digits=36, decimal_places=18, default=0.0)
    locked = models.DecimalField(max_digits=36, decimal_places=18, default=0.0)
    ownusdt = models.DecimalField(max_digits=19, decimal_places=8, default=0.0)
    ownbtc = models.DecimalField(max_digits=19, decimal_places=8, default=0.0)

    def __str__(self):
        return self.asset


class WalletAssetBalance(models.Model):
    time = models.DateTimeField(auto_now=True)
    usdtbalance = models.DecimalField(max_digits=19, decimal_places=8, default=0.0)
    btcbalance = models.DecimalField(max_digits=19, decimal_places=8, default=0.0)



class CryptoBotSettings(models.Model):
    api_key = models.CharField(max_length=100)
    api_secret = models.CharField(max_length=100)
    SECRET_KEY = models.CharField(max_length=100)