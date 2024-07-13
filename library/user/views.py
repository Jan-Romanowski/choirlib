from django.shortcuts import render, redirect
from .forms import SignUpForm  # убедитесь, что этот импорт добавлен

def index(request):
    return render(request, 'user/index.html')

def signIn(request):
    return render(request, 'user/signIn.html')

def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Перенаправление на главную страницу
    else:
        form = SignUpForm()
    return render(request, 'user/signUp.html', {'form': form})
