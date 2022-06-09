from django.contrib import admin


from .models import CoinList, BinanceSymbolList, Wallet, WalletAssetList, WalletAssetBalance, CryptoBotSettings, Ohlcv

# Register your models here.
# from .models import Post


admin.site.register(CoinList)
admin.site.register(BinanceSymbolList)
admin.site.register(Wallet)
admin.site.register(WalletAssetList)
admin.site.register(WalletAssetBalance)
admin.site.register(CryptoBotSettings)
admin.site.register(Ohlcv)
