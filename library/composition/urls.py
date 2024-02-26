from django.urls import path
from . import views

urlpatterns = [
    path('composition', views.index, name='main'),
]
