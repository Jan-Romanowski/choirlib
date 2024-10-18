from django.shortcuts import render
from news.models import News
from event.models import Event
from datetime import date
import random
from django.db.models import Q, Min
from django.utils import timezone

def index(request):
    news = list(News.objects.filter(isActual=True))
    now = timezone.now()  # Текущее время
    closest_date = Event.objects.filter(
        Q(date_event__gt=now.date()) |  # Будущие события
        Q(date_event=now.date(), start_time__gte=now.time())  # Сегодняшние, начиная с текущего времени
    ).aggregate(Min('date_event'))['date_event__min']

    if closest_date:
        events = Event.objects.filter(date_event=closest_date).order_by('start_time')
    else:
        events = []
    random.shuffle(news)
    return render(request, 'content/index2.html', {'news': news, 'events': events, 'date': closest_date})

def sandbox(request):
    return render(request, 'content/bubbles.html')

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