from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignInForm, SignUpForm
from django.contrib import messages

def index(request):
    return render(request, 'user/index.html')


def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Konto pomyślnie załozone.')
            return redirect('/user/signIn')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    else:
        form = SignUpForm()

    return render(request, 'user/signUpForm.html', {'form': form})



def signIn(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Poprawne dane do logowania.')
                return redirect('/')
            else:
                messages.error(request, f'Nieprawidłowe dane do logowania.')
                form.add_error(None, 'Nieprawidłowe dane do logowania')
    else:
        form = SignInForm()

    return render(request, 'user/signInForm.html', {'form': form})