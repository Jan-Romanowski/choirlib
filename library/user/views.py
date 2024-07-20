from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignInForm, SignUpForm

def index(request):
    return render(request, 'user/index.html')


def signUp(request):
    error = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user/signIn')
        else:
            error = 'Пошёл нахуй быдло'

    form = SignUpForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'user/signUpForm.html', data)


def signIn(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  # Перенаправление на домашнюю страницу после успешного входа
            else:
                form.add_error(None, 'Неверные учетные данные')
    else:
        form = SignInForm()

    return render(request, 'user/signInForm.html', {'form': form})