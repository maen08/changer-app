from change_app.models import Amount
from django import forms



class TotalAmountForm(forms.ModelForm):
    total_amount = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter amount'}))

    class Meta:
        fields = ('total_amount',)
        model = Amount


class MultiplierForm(forms.ModelForm):
    class Meta:
        fields = ('multiplier',)
        model = Amount