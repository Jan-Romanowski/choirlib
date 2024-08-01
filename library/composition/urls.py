from django.urls import path
from . import views

urlpatterns = [
    path('list', views.index, name='listComposition'),
    path('edit', views.editComposition, name='editComposition'),
    path('create', views.editComposition, name='createComposition'),
    path('details/<int:id>/', views.detailsComposition, name='detailsComposition'),
]
