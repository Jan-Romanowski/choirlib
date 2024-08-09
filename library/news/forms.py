from django import forms
from .models import News
from django.forms import ModelForm, TextInput

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text']

        labels = {
            'title': 'Nagłówek',
            'text': 'Tekst',
        }

        widgets = {
                'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Jakiś tam nagłówek'
            }),
            'text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Jakiś tam tekst'
            }),
        }