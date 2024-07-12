from django.shortcuts import render

def index(request):
    return render(request, 'user/index.html')


def signIn(request):
    return render(request, 'user/signIn.html')

def signUp(request):
    return render(request, 'user/signUp.html')
