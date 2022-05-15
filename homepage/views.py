from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic.edit import FormMixin
from django.views.generic import TemplateView, ListView, CreateView, DetailView, FormView
from .models import CoinList, BinanceSymbolList, Wallet, WalletAssetList, WalletAssetBalance, CryptoBotSettings
from .forms import CoinListAdd, CoinListDelForm, UpdateBnSymbol, UpdateWalletAsset, UpdateWalletBalance, UpdateCryptoBotSettings
from .scripts.binance_client import get_binance_symbol
from .scripts.wallet import get_wallet_assets, info
from django.http import JsonResponse
import json
from django.core import serializers

# Create your views here.


class HomePageView(TemplateView):
    template_name = "homepage.html"


class CoinListView(ListView):
    model = CoinList
    template_name = "list.html"


class ManageCoinView(ListView):
    model = CoinList
    template_name = "manage-coin.html"


class ManageCoinAddView(CreateView):
    model = BinanceSymbolList
    form_class = CoinListAdd
    template_name = "manage-coin.html"
    coinlist = []


    def get_context_data(self, **kwargs):
        context = super(ManageCoinAddView, self).get_context_data(**kwargs)
        # context["coinlist"] = CoinList.objects.all()
        context = {
            'coinlist': CoinList.objects.all(),
            'symbolist': BinanceSymbolList.objects.all()
    }
        return context

    # def get(self, request, *args, **kwargs):
    #     # symbol = self.get_context_data(**kwargs)
    #     # context = {"form": CoinListAdd(), "symbol": symbol}
    #     # symbol = self.get_context_data(**kwargs)

    #     # coinlist = CoinList.objects.all()
    #     #context = {"form": CoinListAdd(), "coinlist" : coinlist}
    #     context = {"form": CoinListAdd()}
    #     return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        coinlist = CoinList.objects.all()
        addform = self.form_class(request.POST)
        if addform.is_valid():
            addform.save()
            show_text = True
        else:
            show_text = False
        return render(
                request, self.template_name, {"addform": addform, "coinlist": coinlist, "show_text": show_text}
            )





class WalletView(ListView):
    model = CoinList
    template_name = "wallet.html"

    # def get(self, request, *args, **kwargs):
    #     # spot_balance = get_spot_balance()
    #     spot_balance = "AAAAAAAAAAAAAAAAAAAA"
    #     context = {"spot_balance": spot_balance}
    #     return render(request, self.template_name, context)    

    # def get_context_data(self, *args, **kwargs):
    #     spot_balance =  WalletAssetList.objects.values_list('name', flat=True)
    #     return spot_balance

    def get(self, request, *args, **kwargs):
        wallet_asset = WalletAssetList.objects.all()
        wallet_balance = WalletAssetBalance.objects.all()
        context = {"wallet_asset": wallet_asset, "wallet_balance": wallet_balance}
        return render(request, self.template_name, context)
 



class UpdateWalletAssetView(CreateView):
    model = WalletAssetList
    template_name = "wallet.html"
    form_class = UpdateWalletAsset



    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        show_text = True
        asset_list, own_usdt, own_btc = get_wallet_assets(info)
        for index, row in asset_list.iterrows():
            asset = row['asset']
            free = row['free']
            locked = row['locked']
            ownusdt = row['ownusdt']
            ownbtc = row['ownbtc']
            WalletAssetList.objects.update_or_create( \
                            defaults={'free': free, 'locked': locked, \
                            'ownusdt': ownusdt, 'ownbtc': ownbtc}, \
                            asset=asset )
        WalletAssetBalance.objects.create(usdtbalance = own_usdt, btcbalance = own_btc)                    
        return redirect(reverse('WalletView'))                      




class CoinListAdd(CreateView):
    model = BinanceSymbolList
    form_class = CoinListAdd
    template_name = "add.html"

    def get_context_data(self, *args, **kwargs):
        symbol =  BinanceSymbolList.objects.values_list('symbol', flat=True)
        return symbol

    def get(self, request, *args, **kwargs):
        symbol = self.get_context_data(**kwargs)
        context = {"form": CoinListAdd(), "symbol": symbol}
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            CoinList = form.save()
            show_text = True
            return render(
                request, self.template_name, {"form": form, "show_text": show_text}
            )
        else:
            show_text = False
            return render(
                request, self.template_name, {"form": form, "show_text": show_text}
            )


class UpdateBinanceSymbolView(CreateView):
    model = BinanceSymbolList
    form_class = UpdateBnSymbol
    template_name = "manage-coin.html"

    def post(self, request, **kwargs):
        coinlist = CoinList.objects.all()
        symbolist = BinanceSymbolList.objects.all()
        symbol_list = get_binance_symbol()
        symbol_list.sort()
        symbol = CoinListAdd.get_context_data(self)
        symbol = list(symbol)
        symbol.sort()
        if (symbol_list == symbol):
            list_updated = True
            return render(
                request, self.template_name, {"list_updated": list_updated, "coinlist": coinlist, "symbolist": symbolist }
            )
        else:
            new = list(set(symbol_list) - set(symbol))
        BinanceSymbolList.objects.bulk_create([BinanceSymbolList(symbol=x) for x in new])
        show_list_text = True
        return render(
                request, self.template_name, {"show_list_text": show_list_text, "coinlist": coinlist, "symbolist": symbolist}
            )




class CoinListDelView(CreateView):
    form_class = CoinListDelForm
    template_name = "del.html"
    model = CoinList

    def get_context_data(self, *args, **kwargs):
        coin = CoinList.objects.values_list('coin', flat=True)
        return coin

    def get(self, request, *args, **kwargs):
        coin = self.get_context_data(**kwargs)
        context = {"form": CoinListDelForm(), "coin": coin}
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # coin = ""
            # form.save()
            # cryptodel = CryptoList.objects.get(crypto_pair="SDSD")
            # cryptodel.delete()
            show_text = True
            #    return HttpResponseRedirect(reverse_lazy("AddCryptoListView"))
            return render(
                request, self.template_name, {"form": form, "show_text": show_text}
            )
        else:
            show_text = False
            return render(
                request, self.template_name, {"form": form, "show_text": show_text}
            )




class UpdateCryptoBotSettingsView(CreateView):
    model = CryptoBotSettings
    form_class = UpdateCryptoBotSettings
    template_name = "settings.html"

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            show_text = True
            return render(
                request, self.template_name, {"form": form, "show_text": show_text}
            )
        else:
            show_text = False
            return render(
                request, self.template_name, {"form": form, "show_text": show_text}
            )    




def autocompleteAdd(request):
    query_original = request.GET.get('term')
    queryset = BinanceSymbolList.objects.filter(symbol__icontains=query_original)
    mylist = []
    mylist += [x.symbol for x in queryset]
    return JsonResponse(mylist, safe=False)


def autocompleteDel(request):
    query_original = request.GET.get('term')
    queryset = CoinList.objects.filter(coin__icontains=query_original)
    mylist = []
    mylist += [x.coin for x in queryset]
    return JsonResponse(mylist, safe=False)
   