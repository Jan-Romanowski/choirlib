# composition/templatetags/composition_extras.py
from django import template
from django.utils import timezone
from django.utils.timezone import now
from datetime import timedelta

register = template.Library()

@register.filter
def is_audio(file_type):
    return file_type in ['mp3', 'wav']

@register.filter
def is_pdf(file_type):
    return file_type == 'pdf'

@register.filter
def get_filename_without_extension(path):
    """
    Extracts the filename from a path and removes its extension.
    """
    filename = path.rsplit('/', 1)[-1] if '/' in path else path
    return filename.split('.')[0] if '.' in filename else filename

@register.filter
def activity_status(last_activity):
    if last_activity is None:
        return "offline"

    current_time = now()
    time_diff = current_time - last_activity

    if time_diff < timedelta(minutes=5):
        return "online"
    elif time_diff < timedelta(hours=1):
        minutes = time_diff.seconds // 60
        return f"{minutes} minut temu"
    elif time_diff < timedelta(days=1):
        hours = time_diff.seconds // 3600
        return f"{hours} godziny temu" if hours != 1 else "godzina temu"
    elif time_diff < timedelta(days=7):
        days = time_diff.days
        return f"{days} dni temu" if days != 1 else "dzień temu"
    elif time_diff < timedelta(days=150):
        weeks = time_diff.days // 7
        return f"{weeks} tygodni temu" if weeks != 1 else "tydzień temu"
    elif time_diff < timedelta(days=365):
        months = time_diff.days // 30
        return f"{months} miesięcy temu" if months != 1 else "miesiąc temu"
    else:
        years = time_diff.days // 365
        return f"{years} lat temu" if years != 1 else "rok temu"


