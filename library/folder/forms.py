from django import forms
from .models import Folder
from django.forms import ModelForm, TextInput

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name', 'note', 'colour']

        labels = {
                    'name': 'Nazwa',
                    'note': 'Opis',
                    'colour': 'Kolor teczki',
                }

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Czerwona teczka'
            }),
            'note': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Opis'
            }),
            'colour': TextInput(attrs={
                'type' : 'color',
                'class': 'form-control form-control-color',
                'placeholder': 'Kolor teczki'
            }),
        }