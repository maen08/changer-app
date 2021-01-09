from django import forms

from user_app.models import ChangerUser


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = ChangerUser
        fields = ['username', 'phone_number', 'password']


class UserLogin(forms.ModelForm):
    class Meta:
        model = ChangerUser
        fields = ['username', 'password']
