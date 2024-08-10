from django.urls import path
from . import views

urlpatterns = [
    path('list', views.listNews, name='listNews'),
    path('edit/<int:id>/', views.editNews, name='editNews'),
    path('create', views.editNews, name='createNews'),
    path('details/<int:id>/', views.detailsNews, name='detailsNews'),
    path('delete/<int:id>/', views.deleteNews, name='deleteNews'),   
    path('uploadFile/<int:id>/', views.uploadFiles, name='uploadFilesNews'),
    path('deleteFile/<int:id>/', views.deleteNewsFile, name='deleteFileNews'),
    path('setMainPicture/<int:news_file_id>/', views.set_main_image_view, name='set_main_image'),
    path('toggleActual/<int:id>/', views.checkAsActual, name='toggleActualNews'),
]
