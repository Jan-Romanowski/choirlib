from django.urls import path
from . import views

urlpatterns = [
    path('list', views.listComposition, name='listComposition'),
    path('create', views.editComposition, name='createComposition'),
    path('edit/<int:pk>/', views.editComposition, name='editComposition'),
    path('details/<int:id>/', views.detailsComposition, name='detailsComposition'),
    path('delete/<int:pk>/', views.deleteComposition, name='deleteComposition'),
    path('<int:composition_id>/upload/', views.uploadFiles, name='uploadFilesComposition'),
    path('deleteFile/<int:id>/', views.deleteCompositionFile, name='deleteFileComposition'),
    path('<int:id>/toggleActual/', views.checkAsActual, name='toggleActual'),
]
