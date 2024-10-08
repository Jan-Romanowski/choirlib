from django import forms
from .models import News, NewsFile
from django.forms import ModelForm, TextInput

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text', 'date_joined']

        labels = {
            'title': 'Nagłówek',
            'text': 'Tekst',
            'date_joined': 'Data',
        }

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Jakiś tam nagłówek'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Jakiś tam tekst'
            }),
            'date_joined': forms.DateInput(attrs={
                'class': 'form-control mt-2 w-25',
                'type': 'date'
            })

        }

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = NewsFile
        fields = ['file']