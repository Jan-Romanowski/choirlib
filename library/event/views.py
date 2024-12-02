# views.py
import calendar
from datetime import datetime, date, timedelta
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Event
from calendar import monthrange
from django.utils import timezone
from .forms import EventForm
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from datetime import datetime

# views.py

def get_month(request, year, month):
    first_day_of_month = date(year, month, 1)
    _, days_in_month = calendar.monthrange(year, month)
    start_day = first_day_of_month.weekday()  # 0: Monday, 6: Sunday

    days = []
    for day in range(1, days_in_month + 1):
        current_date = date(year, month, day)
        events = Event.objects.filter(date_event=current_date).order_by('start_time')
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

@permission_required('event.deleve_event', raise_exception=True)
def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    return redirect('calendar')

def calendar_view(request):
    events = Event.objects.all().order_by('start_time')
    return render(request, 'calendar.html', {'events': events})

@permission_required('event.change_event', raise_exception=True)
def day_events_form(request, year, month, day):
    selected_date = timezone.datetime(year, month, day).date()
    events = Event.objects.filter(date_event=selected_date).order_by('start_time')

    unique_colours = (Event.objects
                      .values('colour')
                      .distinct()
                      .order_by('-date_event')[:20])

    savedColors = []
    for color in unique_colours:
        if color not in savedColors:
            savedColors.append(color)

    if request.method == 'POST':
        # Удаление события
        if 'delete_event' in request.POST:
            event_id = request.POST.get('event_id')
            event = get_object_or_404(Event, id=event_id)
            event.delete()
            messages.success(request, f'Wydarzenie pomyślnie usunięte.')
            return redirect('day_events_form', year=year, month=month, day=day)

        # Проверяем, редактируем или создаём
        event_id = request.POST.get('event_id')
        if event_id:
            # Редактирование события
            event = get_object_or_404(Event, id=event_id)
            form = EventForm(request.POST, instance=event)
        else:
            # Создание нового события
            form = EventForm(request.POST)

        if form.is_valid():
            new_event = form.save(commit=False)
            new_event.date_event = selected_date

            # Проверяем, отмечен ли чекбокс 'cycle'
            if 'cycle' in request.POST and request.POST.get('cycleDate'):
                cycle_date_str = request.POST.get('cycleDate')
                cycle_end_date = timezone.datetime.strptime(cycle_date_str, '%Y-%m-%d').date()

                current_date = selected_date
                while current_date <= cycle_end_date:
                    new_event.pk = None
                    new_event.date_event = current_date
                    new_event.save()
                    current_date += timedelta(days=7)

                messages.success(request, f'Dodano cykliczne wydarzenie każdy tydzień do {cycle_end_date}.')
            else:
                new_event.save()
                if event_id:
                    messages.success(request, f'Wydarzenie zostało zaktualizowane.')
                else:
                    messages.success(request, f'Dodano nowe wydarzenie.')
                    
            return redirect('day_events_form', year=year, month=month, day=day)
    else:
        form = EventForm()

    context = {
        'date': selected_date,
        'events': events,
        'form': form,
        'colors': savedColors
    }
    return render(request, 'event/day_events_form.html', context)



def export_events_to_ics(request):
    events = Event.objects.all()
    
    # Создание содержимого файла iCalendar
    ics_content = "BEGIN:VCALENDAR\n"
    ics_content += "VERSION:2.0\n"
    ics_content += "CALSCALE:GREGORIAN\n"

    for event in events:
        ics_content += "BEGIN:VEVENT\n"
        ics_content += f"SUMMARY:{event.title}\n"
        ics_content += f"DESCRIPTION:{event.description}\n"
        ics_content += f"DTSTART;TZID=Europe/Warsaw:{event.date_event.strftime('%Y%m%d')}T{event.start_time.strftime('%H%M%S')}\n"
        ics_content += f"DTEND;TZID=Europe/Warsaw:{event.date_event.strftime('%Y%m%d')}T{event.end_time.strftime('%H%M%S')}\n"
        ics_content += "END:VEVENT\n"

    ics_content += "END:VCALENDAR\n"

    # Создание HTTP-ответа с содержимым файла iCalendar
    response = HttpResponse(ics_content, content_type='text/calendar')
    response['Content-Disposition'] = 'attachment; filename="events.ics"'
    return response

def day_events(request, year, month, day):
    selected_date = timezone.datetime(year, month, day).date()
    events = Event.objects.filter(date_event=selected_date).order_by('start_time')

    context = {
        'date': selected_date,
        'selected_day':day,
        'selected_month': month,
        'selected_year': year,
        'events': events
    }

    return render(request, 'event/day_events.html', context)