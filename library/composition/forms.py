from .models import Composition
from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput

class CompositionForm(ModelForm):
    class Meta:
        model = Composition
        fields = ['name', 'author', 'number', 'folder', 'note']

        labels = {
            'name': 'Nazwa',
            'author': 'Autor',
            'number': 'Numer',
            'folder': 'Teczka',
            'note': 'Notatki'
        }

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ich will'
            }),
            'Autor': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rammstein'
            }),
            'number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Numer utworu'
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