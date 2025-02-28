from django import forms
from django.contrib.auth.forms import AuthenticationForm


class AddURLForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Назва')
    url = forms.URLField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Посилання')

