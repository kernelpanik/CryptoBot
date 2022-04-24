from django.urls import path, include
from .views import (
    HomePageView,
    CoinList,
    CoinListAdd,
    CoinListDelView,
    UpdateBinanceSymbolView,
    WalletView,
    UpdateWalletAssetView
)




urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("wallet", WalletView.as_view(), name="WalletView"),
    path("Coin/list.html", CoinList.as_view(), name="CoinList"),
    path("Coin/add.html", CoinListAdd.as_view(), name="CoinListAdd"),
    path("Coin/del.html", CoinListDelView.as_view(), name="CoinListDel"),
    path("Coin/UpdateBinanceSymbol/", UpdateBinanceSymbolView.as_view(), name="UpdateBinanceSymbol"),
    path("Wallet/Update_Asset/", UpdateWalletAssetView.as_view(), name="UpdateWalletAsset"),
]
