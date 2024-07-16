from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
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
            # Получение данных пользователя из формы
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Аутентификация пользователя
            user = authenticate(request, username=email, password=password)
            if user is not None:
                # Вход пользователя
                login(request, user)
                # Перенаправление на страницу после успешной авторизации
                return redirect('success_page')
            else:
                # Обработка ошибки аутентификации
                # Например, вывод сообщения об ошибке
                return render(request, 'user/signInForm.html', {'form': form, 'error_message': 'Invalid credentials'})
    else:
        form = SignInForm()
    
    return render(request, 'user/signInForm.html', {'form': form})