from django.urls import path, include
from . import views

from .views import (
    HomePageView,
    CoinListView,
    CoinListAdd,
    CoinListDelView,
    UpdateBinanceSymbolView,
    WalletView,
    UpdateWalletAssetView,
    UpdateCryptoBotSettingsView,
    ManageCoinView,
    ManageCoinAddView,
    autocompleteAdd,
    autocompleteDel
)




urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("wallet.html", WalletView.as_view(), name="WalletView"),
#    path("manage-coin.html", ManageCoinView.as_view(), name="ManageCoinView"),
    path("manage-coin.html", ManageCoinAddView.as_view(), name="ManageCoinAddView"),
    path("manage-coin.html/update-binance-list/", UpdateBinanceSymbolView.as_view(), name="UpdateBinanceSymbol"),
    path("Coin/list.html", CoinListView.as_view(), name="CoinList"),
    path("Coin/add.html", CoinListAdd.as_view(), name="CoinListAdd"),
    path("Coin/del.html", CoinListDelView.as_view(), name="CoinListDel"),
#    path("Coin/UpdateBinanceSymbol/", UpdateBinanceSymbolView.as_view(), name="UpdateBinanceSymbol"),
    path("Wallet/Update_Asset/", UpdateWalletAssetView.as_view(), name="UpdateWalletAsset"),
    path("settings.html", UpdateCryptoBotSettingsView.as_view(), name="UpdateCryptoBotSettings"),
    path('autocompleteAdd', views.autocompleteAdd, name='autocompleteAdd'),
    path('autocompleteDel', views.autocompleteDel, name='autocompleteDel')
]
