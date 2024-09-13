from django import forms
from .models import Repertoir
from django.forms import ModelForm, TextInput

class RepertoirForm(forms.ModelForm):
    class Meta:
        model = Repertoir
        fields = ['title', 'text']

        labels = {
            'title': 'Nagłówek',
            'text': 'Tekst',
        }

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rammstein'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Notatki',
                'style' : 'height: 150px;'
            }),
        }
        