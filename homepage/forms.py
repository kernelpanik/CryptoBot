from django import forms
from .models import CoinList, BinanceSymbolList, WalletAssetList, WalletAssetBalance, CryptoBotSettings



class CoinListAdd(forms.ModelForm):
    class Meta:
        model = CoinList
        label = "coin"
        fields = ["coin"]
        widgets = {
            "coin": forms.TextInput(attrs={"placeholder": "ex. BTCUSDT"}),
        }

    def __init__(self, *args, **kwargs):
        super(CoinListAdd, self).__init__(*args, **kwargs)

    def clean(self):
        data = self.cleaned_data["coin"]
        if data.islower() or (not data.islower() and not data.isupper()):
            data = data.upper()
        if not BinanceSymbolList.objects.filter(symbol=data).exists():
            raise forms.ValidationError(
                    "Coin "
                    + data
                    + " not found"
                )
        if CoinList.objects.filter(coin=data).exists():
            raise forms.ValidationError(
                "Coin "
                + data
                + " has already been added"
            )
        return super(CoinListAdd, self).clean()



class CoinListDelForm(forms.ModelForm):
    class Meta:
        model = CoinList
        label = "coin"
        fields = ["coin"]
        widgets = {
            "coin": forms.TextInput(attrs={"placeholder": "ex. ADAUSDT"}),
        }

    def __init__(self, *args, **kwargs):
        super(CoinListDelForm, self).__init__(*args, **kwargs)

    def clean(self):
        data = self.cleaned_data["coin"]
        if data.islower() or (not data.islower() and not data.isupper()):
            data = data.upper()
            self.cleaned_data["coin"] = data
        if CoinList.objects.filter(coin=data).exists():
            CoinList.objects.filter(coin=data).delete()
        else:
            raise forms.ValidationError(
                "Cryptocurrency pair " + self.cleaned_data["coin"] + " not found"
            )
        return super(CoinListDelForm, self).clean()





class UpdateBnSymbol(forms.ModelForm):
    class Meta:
        model = BinanceSymbolList
        label = "symbol"
        fields = ["symbol"]

    def __init__(self, *args, **kwargs):
        super(UpdateBnSymbol, self).__init__(*args, **kwargs)



class UpdateWalletAsset(forms.ModelForm):
    class Meta:
        model = WalletAssetList
        label = "asset"
        fields = ["asset", "free", "locked", "ownusdt", "ownbtc"]

    def __init__(self, *args, **kwargs):
        super(UpdateWalletAsset, self).__init__(*args, **kwargs)


class UpdateWalletBalance(forms.ModelForm):
    class Meta:
        model = WalletAssetBalance
        fields = ["usdtbalance", "btcbalance"]

    def __init__(self, *args, **kwargs):
        super(UpdateWalletBalance, self).__init__(*args, **kwargs)





class UpdateCryptoBotSettings(forms.ModelForm):
    class Meta:
        model = CryptoBotSettings
        fields = ["api_key", "api_secret", "SECRET_KEY"]

    def __init__(self, *args, **kwargs):
        super(UpdateCryptoBotSettings, self).__init__(*args, **kwargs)

    def clean(self):
        if CryptoBotSettings.objects.exists():
            print("here")
            raise forms.ValidationError('You cannot add more somethings.')
#        return super(UpdateCryptoBotSettings, self).clean()
    


