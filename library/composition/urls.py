from django.urls import path
from . import views

urlpatterns = [
    path('list', views.index, name='listComposition'),
    path('create', views.editComposition, name='createComposition'),
    path('edit/<int:pk>/', views.editComposition, name='editComposition'),
    path('details/<int:id>/', views.detailsComposition, name='detailsComposition'),
    path('delete/<int:pk>/', views.deleteComposition, name='deleteComposition'),
]
