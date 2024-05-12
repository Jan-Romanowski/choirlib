from django.urls import path
from . import views

urlpatterns = [
    path('userList', views.userList, name='userList'),
    path('signUp', views.signUp, name='signUp'),
    path('signIn', views.signIn, name='signIn'),
]
