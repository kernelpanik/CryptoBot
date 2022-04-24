from django.contrib import admin


from .models import CoinList, BinanceSymbolList, Wallet, WalletAssetList

# Register your models here.
# from .models import Post


admin.site.register(CoinList)
admin.site.register(BinanceSymbolList)
admin.site.register(Wallet)
admin.site.register(WalletAssetList)
