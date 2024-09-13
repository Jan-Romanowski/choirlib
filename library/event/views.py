# views.py
import calendar
from datetime import datetime, date
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Event
from calendar import monthrange
from django.utils import timezone
from .forms import EventForm

# views.py

def get_month(request, year, month):
    first_day_of_month = date(year, month, 1)
    _, days_in_month = calendar.monthrange(year, month)
    start_day = first_day_of_month.weekday()  # 0: Monday, 6: Sunday

    days = []
    for day in range(1, days_in_month + 1):
        current_date = date(year, month, day)
        events = Event.objects.filter(date_event=current_date)
        days.append({
            'day': day,
            'date': current_date,
            'events': events
        })

    today = timezone.localdate()

    days_of_week = ["Pn", "Wt", "Śr", "Cz", "Pt", "So", "N"]

    context = {
        'days_in_month': days,
        'empty_days': range(start_day),
        'prev_month': first_day_of_month.replace(day=1) - timezone.timedelta(days=1),
        'next_month': first_day_of_month.replace(day=days_in_month) + timezone.timedelta(days=1),
        'days_of_week': days_of_week,
        'current_year': year,
        'current_month': month,
        'current_month_object' : first_day_of_month,
        'today' : today
    }
    return render(request, 'event/calendar.html', context)

def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    return redirect('calendar')

def calendar_view(request):
    events = Event.objects.all().order_by('start_time')
    return render(request, 'calendar.html', {'events': events})

def day_events(request, year, month, day):

    selected_date = timezone.datetime(year, month, day).date()
    events = Event.objects.filter(date_event=selected_date)

    unique_colours = (Event.objects
                  .values('colour')              # Извлекаем только поле цвета
                  .distinct()                    # Убираем дубли
                  .order_by('-date_event')       # Сортировка по дате (сначала самые новые)
                  [:20])
    
    savedColors = []
    
    for color in unique_colours:
        if color not in savedColors:
            savedColors.append(color)

    if request.method == 'POST':
        if 'delete_event' in request.POST:
            event_id = request.POST.get('event_id')
            event = get_object_or_404(Event, id=event_id)
            event.delete()
            messages.success(request, f'Wydarzenie pomyślnie usunięte.')
            return redirect('day_events', year=year, month=month, day=day)
        
        form = EventForm(request.POST)
        if form.is_valid():
            new_event = form.save(commit=False)
            new_event.date_event = selected_date  # Устанавливаем дату события
            new_event.save()
            messages.success(request, f'Dodano nowe wydarzenie.')
            return redirect('day_events', year=year, month=month, day=day)
    else:
        form = EventForm()

    context = {
        'date': selected_date,
        'events': events,
        'form': form,
        'colors': savedColors
    }
    return render(request, 'event/day_events.html',  context)