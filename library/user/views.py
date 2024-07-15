from django.shortcuts import render, redirect

from .forms import UsersForm
from .models import Users


def index(request):
    return render(request, 'user/index.html')


def userList(request):
    users = Users.objects.all()
    return render(request, 'user/userList.html', {'users': users})


def signUp(request):
    error = ''
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Пошёл нахуй быдло'

    form = UsersForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'user/signUpForm.html', data)


def signIn(request):
    return render(request, 'user/signInForm.html')
