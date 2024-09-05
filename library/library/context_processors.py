from django.utils import timezone

def current_time(request):
    now = timezone.now()
    return {
        'current_year': now.year,
        'current_month': now.month,
    }