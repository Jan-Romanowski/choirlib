from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from .models import User
from django.contrib.auth.models import Permission

class SignUpForm(forms.ModelForm):
    password_confirm = forms.CharField(
        label='Potwierdź hasło', 
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Powtórz hasło'
        })
    )

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
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@example.com'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Wpisz imię'
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Wpisz nazwisko'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Haslo123'
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Проверка на уникальность email
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email jest już używany.')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError('Hasło musi mieć co najmniej 8 znaków.')
        if not any(char.isdigit() for char in password):
            raise ValidationError('Hasło musi zawierać co najmniej jedną cyfrę.')
        if not any(char.islower() for char in password):
            raise ValidationError('Hasło musi zawierać co najmniej jedną małą literę.')
        if not any(char.isupper() for char in password):
            raise ValidationError('Hasło musi zawierać co najmniej jedną wielką literę.')
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        # Проверка, что пароли совпадают
        if password != password_confirm:
            raise ValidationError('Hasła nie są takie same.')

        return cleaned_data

class SignInForm(forms.Form):
    email = forms.EmailField(
        label='Email', 
        max_length=100,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'example@example.com'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
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
