from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, DetailView, FormView
from .models import CoinList, BinanceSymbolList, Ohlcv, Wallet, WalletAssetList, WalletAssetBalance, CryptoBotSettings
from .forms import CoinListAdd, CoinListDelForm, UpdateBnSymbol, UpdateWalletAsset, UpdateWalletBalance, UpdateCryptoBotSettings
from .scripts.binance_client import get_binance_symbol, get_old_ohlcv
from .scripts.wallet import get_wallet_assets, get_binance_savings, get_binance_locked_stacking, \
get_binance_flex_defi_stacking, get_binance_locked_defi_stacking, info
from django.http import JsonResponse
import datetime
from django.conf import settings
from django.shortcuts import get_object_or_404

# Create your views here.


class HomePageView(TemplateView):
    template_name = "homepage.html"

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

    def post(self, request, **kwargs):
        symbolist = BinanceSymbolList.objects.all()
        coinlist = CoinList.objects.all()
        if 'coinadd' in request.POST:
            addform = self.form_class(request.POST)
            if addform.is_valid():
                addform.save()
                show_text = True
            else:
                show_text = False
            return render(
                request, self.template_name, {"addform": addform, "coinlist": coinlist, "show_text": show_text, "symbolist": symbolist}
                )


class ManageCoinDelView(CreateView):
    template_name = "manage-coin.html"
    form_class = CoinListDelForm
    model = CoinList

    def post(self, request, **kwargs):
        coinlist = CoinList.objects.all()
        symbolist = BinanceSymbolList.objects.all()
        delform = self.form_class(request.POST)
        if delform.is_valid():
            # delform.save()
            show_del_text = True
            return render(
                request, self.template_name, {"delform": delform, "coinlist": coinlist, "symbolist": symbolist, "show_del_text": show_del_text}
            )
        else:
            return render(
                request, self.template_name, {"delform": delform, "coinlist": coinlist, "symbolist": symbolist}
            )                
  

class WalletView(ListView):
    model = CoinList
    template_name = "wallet.html"

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
        save_balance = get_binance_savings()
        btc_save = save_balance['totalAmountInBTC']
        usdt_save = save_balance['totalAmountInUSDT']
        locked_stake_usdt, locked_stake_btc = get_binance_locked_stacking()
        flex_defi_stake_usdt, flex_defi_stake_btc = get_binance_flex_defi_stacking()
        locked_defi_stake_usdt, locked_defi_stake_btc = get_binance_locked_defi_stacking()
        asset_list, spot_usdt, spot_btc = get_wallet_assets(info)
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
        usdt_tot = float(usdt_save) + float(spot_usdt) + float(locked_stake_usdt)
        btc_tot = float(btc_save) + float(spot_btc) + float(locked_stake_btc)

        usdt_stake = locked_stake_usdt + flex_defi_stake_usdt + locked_defi_stake_usdt
        btc_stake = locked_stake_btc + flex_defi_stake_btc + locked_defi_stake_btc
        WalletAssetBalance.objects.create(usdtspot = spot_usdt, btcspot = spot_btc, usdtsav = usdt_save, btcsav = btc_save, 
                usdtbal = usdt_tot, btcbal = btc_tot, usdtstake = usdt_stake, btcstake = btc_stake )                    
        return redirect(reverse('WalletView'))                      


class UpdateBinanceSymbolView(CreateView):
    model = BinanceSymbolList
    form_class = UpdateBnSymbol
    template_name = "manage-coin.html"

    def post(self, request, **kwargs):
        coinlist = CoinList.objects.all()
        symbolist = BinanceSymbolList.objects.all()
        symbol_list = get_binance_symbol()
        symbol_list.sort()
        symbol = BinanceSymbolList.objects.values_list('symbol', flat=True)
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
   


class CryptoDetailView(DetailView):
    model = CoinList
    template_name = "detail.html"

    def get(self, request, *args, **kwargs):
        asset = self.kwargs.get("slug")
        obj = Ohlcv.objects.filter(coin=asset)
        if not obj.exists():
            messageno = "No OHLCV data found"
            messageok = ""
        else:
            messageok = "OHLCV data found"
            messageno = ""    
        context = {"asset": asset, "messageok": messageok, "messageno": messageno}
        return render(request, self.template_name, context)


   

def SearchResults(request, search):
    search = request.GET.get('search')
    response = redirect('/dashboard/%s' % search)
    return response


###### cookie - to fix
######################
# def set_cookie(response, key, value, days_expire=7):
#     if days_expire is None:
#         max_age = 365 * 24 * 60 * 60  # one year
#     else:
#         max_age = days_expire * 24 * 60 * 60
#     expires = datetime.datetime.strftime(
#         datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
#         "%a, %d-%b-%Y %H:%M:%S GMT",
#     )
#     response.set_cookie(
#         key,
#         value,
#         max_age=max_age,
#         expires=expires,
#         domain=settings.SESSION_COOKIE_DOMAIN,
#         secure=settings.SESSION_COOKIE_SECURE or None,
#     )

# def view(request):
#     response = HttpResponse("hello")
#     set_cookie(response, 'name', 'jujule')
#     return response
######################
######################    



class GetOldOhlcvView(CreateView):
    model = CoinList
    template_name = "detail.html"
    
    def post(self, request, **kwargs):
        slug = self.kwargs['asset']
        # if get_old_ohlcv(slug):
        #     message = "No old OHLCV data found"
        #     print(message)
        # if price exsists
            # get 200 days of ohclv
        # else
        #   get only last day  
        # return redirect(reverse('WalletView'))

        get_old_ohlcv(slug)
        # if form.is_valid():
        #     form.save()
        #     show_text = True
        #     return render(
        #         request, self.template_name, {"form": form, "show_text": show_text}
        #     )
        # else:
        #     show_text = False
        #     return render(
        #         request, self.template_name, {"form": form, "show_text": show_text}
        #     ) 
        # show_text = False
        # return render(
        # request, self.template_name, {"show_text": show_text}
        # )
        asset = slug
        context = {
        "asset": asset 
        }
        return render(
        request, self.template_name, context
        )

        #return redirect('CryptoDetails', slug=slug) 