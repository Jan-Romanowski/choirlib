from .models import User
from django import forms
from django.contrib.auth import login, authenticate
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django.contrib.auth.models import Permission

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

class SignInForm(forms.Form):
    email = forms.EmailField(
        label='Email', 
        max_length=100,
        widget=EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'example@example.com'
        })
    )
    password = forms.CharField(
        widget=PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Haslo123'
        }),
        label='Hasło'
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if email and password:
            user = authenticate(email=email, password=password)
            if user is None:
                raise forms.ValidationError("Nieprawidłowe dane do logowania.")
            

class UserPermissionsForm(forms.ModelForm):
    user_permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Permissions"
    )

    class Meta:
        model = User
        fields = ['user_permissions']

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id', None)
        super().__init__(*args, **kwargs)
        if user_id:
            user = User.objects.get(pk=user_id)
            self.fields['user_permissions'].initial = user.user_permissions.all()

