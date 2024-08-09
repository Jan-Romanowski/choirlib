from django.urls import path
from . import views

urlpatterns = [
    path('list', views.listNews, name='listNews'),
    path('edit', views.editNews, name='editNews'),
    path('create', views.editNews, name='createPost'),
]
