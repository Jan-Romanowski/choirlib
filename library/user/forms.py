from .models import User
from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput

class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'surname', 'password']

        labels = {
            'email': 'Email',
            'name': 'Imię',
            'surname': 'Nazwisko',
            'password': 'Hasło',
        }

        widgets = {
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@example.com'
            }),
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Wpisz imię'
            }),
            'surname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Wpisz nazwisko'
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Haslo123'
            }),
        }

class SignInForm(ModelForm):
    class Meta:
        model = User

        username = forms.EmailField(label='Email', max_length=100)


        fields = ['email', 'password']

        labels = {
            'email': 'Email',
            'password': 'Hasło'
        }

        widgets = {
            'email': EmailInput(attrs={
                'class': 'form-control'
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control'
            }),
        }


        # name = models.CharField('name', max_length=25)
        # surname = models.CharField('surname', max_length=25)
        # email = models.CharField('email', max_length=30)
        # password = models.CharField('password', max_length=51)
        # rank = models.CharField('rank', max_length=10)
        # date = models.DateTimeField('regDate')
