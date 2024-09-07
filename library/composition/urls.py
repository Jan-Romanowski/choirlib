from django.urls import path
from . import views

urlpatterns = [
    path('list', views.listComposition, name='listComposition'),
    path('create', views.editComposition, name='createComposition'),
    path('edit/<int:id>/', views.editComposition, name='editComposition'),
    path('details/<int:id>/', views.detailsComposition, name='detailsComposition'),
    path('delete/<int:id>/', views.deleteComposition, name='deleteComposition'),
    path('uploadFile/<int:id>/', views.uploadFiles, name='uploadFilesComposition'),
    path('deleteFile/<int:id>/', views.deleteCompositionFile, name='deleteFileComposition'),
    path('toggleActual/<int:id>/', views.checkAsActual, name='toggleActual'),
    path('search', views.search_compositions, name='search_compositions'),
    path('save_filters', views.save_filters, name='save_filters'),
]
