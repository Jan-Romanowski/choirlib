# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('<int:year>/<int:month>/', views.get_month, name='calendar'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('<int:year>/<int:month>/<int:day>/', views.day_events, name='day_events'),
    path('export_events/', views.export_events_to_ics, name='export_events'),
]
