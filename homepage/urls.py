from django.urls import path, include
from . import views

from .views import (
    HomePageView,
    UpdateBinanceSymbolView,
    WalletView,
    UpdateWalletAssetView,
    UpdateCryptoBotSettingsView,
    ManageCoinAddView,
    ManageCoinDelView,
    CryptoDetailView,
    autocompleteAdd,
    autocompleteDel,
    SearchResults
)




urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("wallet.html", WalletView.as_view(), name="WalletView"),
    path("manage-coin.html", ManageCoinAddView.as_view(), name="ManageCoinAddView"),
    path("manage-coin.html/update-binance-list/", UpdateBinanceSymbolView.as_view(), name="UpdateBinanceSymbol"),
    path("manage-coin.html/delete-coin/", ManageCoinDelView.as_view(), name="ManageCoinDelView"),
    path("Wallet/Update_Asset/", UpdateWalletAssetView.as_view(), name="UpdateWalletAsset"),
    path("settings.html", UpdateCryptoBotSettingsView.as_view(), name="UpdateCryptoBotSettings"),
    path('autocompleteAdd', views.autocompleteAdd, name='autocompleteAdd'),
    path('autocompleteDel', views.autocompleteDel, name='autocompleteDel'),
    path("dashboard/<slug:slug>/", CryptoDetailView.as_view(), name="CryptoDetails"),
    path("search/<str:coin>/", views.SearchResults, name= "SearchResults")

]
