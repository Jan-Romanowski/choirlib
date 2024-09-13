from django import forms
from folder.models import Folder
from .models import Composition, CompositionFile
from django.forms import ModelForm, Select, TextInput

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
            'folder': Select(attrs={
                'class': 'form-select'  # Используйте 'form-select' для стилизации select с Bootstrap
            }),
            'note': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Notatki',
                'style' : 'height: 100px;'
            }),
        }

        folder = forms.ModelChoiceField(queryset=Folder.objects.all(), required=False, empty_label="Wybierz teczkę")

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = CompositionFile
        fields = ['file']