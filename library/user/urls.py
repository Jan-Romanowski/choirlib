from django.urls import path
from . import views

urlpatterns = [
    path('signUp', views.signUp, name='signUp'),
    path('signIn', views.signIn, name='signIn'),
]
