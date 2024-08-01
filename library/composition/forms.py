from .models import Composition
from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput

class CompositionForm(ModelForm):
    class Meta:
        model = Composition
        fields = ['name', 'author', 'folder', 'note']

        labels = {
            'name': 'Nazwa',
            'author': 'Autor',
            'folder': 'Teczka',
            'note': 'Notatki'
        }

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ich will'
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rammstein'
            }),
            'folder': TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'note': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Notatki'
            }),
        }