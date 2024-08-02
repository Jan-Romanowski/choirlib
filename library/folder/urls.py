from django.urls import path
from . import views

urlpatterns = [
    path('list', views.listFolder, name='listFolder'),
    path('create', views.editFolder, name='createFolder'),
    path('edit/<int:pk>/', views.editFolder, name='editFolder'),
    path('details/<int:id>/', views.detailsFolder, name='detailsFolder'),
    path('delete/<int:pk>/', views.deleteFolder, name='deleteFolder'),
]




