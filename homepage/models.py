from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class CoinList(models.Model):
    coin = models.CharField(max_length=15, primary_key=True)
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
    time = models.TimeField(auto_now=True, primary_key=True)
    asset =  models.CharField(max_length=15)
    free = models.DecimalField(max_digits=36, decimal_places=18, default=0.0)
    locked = models.DecimalField(max_digits=36, decimal_places=18, default=0.0)
    ownusdt = models.DecimalField(max_digits=19, decimal_places=8, default=0.0)
    ownbtc = models.DecimalField(max_digits=19, decimal_places=8, default=0.0)

    def __str__(self):
        return self.asset


class WalletAssetBalance(models.Model):
    time = models.DateTimeField(auto_now=True, primary_key=True)
    usdtbal = models.DecimalField(max_digits=19, decimal_places=8, default=0.0)
    btcbal = models.DecimalField(max_digits=19, decimal_places=8, default=0.0)
    usdtspot = models.DecimalField(max_digits=19, decimal_places=8, default=0.0)
    btcspot = models.DecimalField(max_digits=19, decimal_places=8, default=0.0)
    usdtsav = models.DecimalField(max_digits=19, decimal_places=8, default=0.0)
    btcsav = models.DecimalField(max_digits=19, decimal_places=8, default=0.0)
    usdtstake = models.DecimalField(max_digits=19, decimal_places=8, default=0.0)
    btcstake = models.DecimalField(max_digits=19, decimal_places=8, default=0.0)



class CryptoBotSettings(models.Model):
    api_key = models.CharField(max_length=100, null=True)
    api_secret = models.CharField(max_length=100, null=True)
    SECRET_KEY = models.CharField(max_length=100, null=True)
    mysql_host = models.GenericIPAddressField(null=True)
    mysql_db_name = models.CharField(max_length=100, null=True)
    mysql_user = models.CharField(max_length=100, null=True) 
    mysql_pwd = models.CharField(max_length=100, null=True)




class Ohlcv(models.Model):
    coin = models.OneToOneField(CoinList,on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=timezone.now, primary_key=True)
    open = models.DecimalField(max_digits=36, decimal_places=18, null=True)
    high = models.DecimalField(max_digits=36, decimal_places=18, null=True)
    low = models.DecimalField(max_digits=36, decimal_places=18, null=True)
    close = models.DecimalField(max_digits=36, decimal_places=18, null=True)
    volume = models.DecimalField(max_digits=36, decimal_places=18, null=True)
    num_trades = models.DecimalField(max_digits=36, decimal_places=18, null=True)
    taker_base_vol = models.DecimalField(max_digits=36, decimal_places=18, null=True)
    taker_quote_vol = models.DecimalField(max_digits=36, decimal_places=18, null=True)


    def __str__(self):
        return self.coin