from django.urls import path
from . import views

urlpatterns = [
    path('list', views.listNews, name='listNews'),
    path('edit/<int:id>/', views.editNews, name='editNews'),
    path('create', views.editNews, name='createNews'),
    path('details/<int:id>/', views.detailsNews, name='detailsNews'),
    path('delete/<int:id>/', views.deleteNews, name='deleteNews'),    
]
