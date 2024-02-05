from django.shortcuts import render
from django.http import HttpResponse

# Главная страница
def index(request): 
    return render(request, 'content/index.html')

# Zarząd Chóru
def managers(request):
    return render(request, 'content/managers.html')