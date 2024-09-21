# composition/templatetags/composition_extras.py
from django import template
from django.utils import timezone
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
    
    now = timezone.now()
    time_diff = now - last_activity

    if time_diff < timedelta(minutes=5):
        return "online"
    else:
        return f"{time_diff.seconds // 60} minut temu"