# forms.py

from django import forms
from .models import Event
from django.forms import ModelForm, TextInput, TimeInput

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_time', 'end_time', 'colour']

        labels = {
            'title': 'Nazwa',
            'description': 'Opis',
            'start_time' : 'Czas rozpoczęcia',
            'end_time' : 'Czas końcowy',
            'colour': 'Kolor',
        }
        
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nazwa wydarzenia'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Opis',
                'style' : 'height: 100px;'
            }),
            'colour': TextInput(attrs={
                'type' : 'color',
                'class': 'form-control form-control-color',
                'placeholder': 'Kolor (w kalendarzu)',
                'id': 'clr'
            }),
            'start_time': TimeInput(attrs={
                'type': 'time',
                'class': 'form-control w-25',
                'placeholder': 'HH:MM',
            }),
            'end_time': TimeInput(attrs={
                'type': 'time',
                'class': 'form-control w-25',
                'placeholder': 'HH:MM',
            }),

        }