from django import forms
from .models import Claim
from django.forms import ModelForm

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

def clean_password2(self):
    cd = self.cleaned_data
    if cd['password'] != cd['password2']:
        raise forms.ValidationError('Пароли не совпадают.')
    return cd['password2']

class ClaimForm(ModelForm):
    class Meta:
        model = Claim
        fields = ['name', 'surname', 'age', 'work', 'wage', 'aim', 'mail', 'status']



