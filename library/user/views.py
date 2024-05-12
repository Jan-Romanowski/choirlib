from django.shortcuts import render
from .models import Users

def index(request):
    return render(request, 'user/index.html')

def userList(request):
    users = Users.objects.all()
    return render(request, 'user/userList.html', {'users': users})

def signUp(request):
    return render(request, 'user/signUpForm.html')

def signIn(request):
    return render(request, 'user/signInForm.html')
