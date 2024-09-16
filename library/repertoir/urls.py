from django.urls import path
from . import views

urlpatterns = [
    path('list', views.listRepertoirs, name='listRepertoirs'),
    path('add', views.editRepertoir, name='addRepertoir'),
    path('edit/<int:pk>/', views.editRepertoir, name='editRepertoir'),
    path('delete/<int:pk>/', views.deleteRepertoir, name='deleteRepertoir'),
]