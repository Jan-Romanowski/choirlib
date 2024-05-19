from .models import Users
from django.forms import ModelForm, TextInput


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['email', 'name', 'surname', 'password']

        widgets = {
            "title": TextInput(attrs={
                'class': '',
                'placeholder': ''
            })
        }

        # name = models.CharField('name', max_length=25)
        # surname = models.CharField('surname', max_length=25)
        # email = models.CharField('email', max_length=30)
        # password = models.CharField('password', max_length=51)
        # rank = models.CharField('rank', max_length=10)
        # date = models.DateTimeField('regDate')
