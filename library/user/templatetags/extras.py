from django import template
from django.utils import timezone
from datetime import timedelta

register = template.Library()

@register.filter
def activity_status(last_activity):
    if last_activity is None:
        return "offline"
    
    now = timezone.now()
    time_diff = now - last_activity

    if time_diff < timedelta(minutes=1):
        return "online"
    else:
        return f"{time_diff.seconds // 60} minut temu"
