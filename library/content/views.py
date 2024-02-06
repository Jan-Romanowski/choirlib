from django.shortcuts import render


def index(request):
    return render(request, 'content/index.html')


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
