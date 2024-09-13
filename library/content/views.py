from django.shortcuts import render
from news.models import News

def index(request):
    news = News.objects.all()
    return render(request, 'content/index.html', {'news': news})


def managers(request):
    return render(request, 'content/managers.html')


def news(request):
    return render(request, 'content/news.html')


def contact(request):
    return render(request, 'content/contact.html')


def conductor(request):
    return render(request, 'content/conductor.html')


def viceConductor(request):
    return render(request, 'content/viceConductor.html')


def history(request):
    return render(request, 'content/history.html')


def hoffman(request):
    return render(request, 'content/hoffman.html')

def custom_permission_denied_view(request, exception):
    return render(request, 'content/403.html', status=403)