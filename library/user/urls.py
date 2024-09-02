from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('signUp', views.signUp, name='signUp'),
    path('signIn', views.signIn, name='signIn'),
    path('details/<int:id>/', views.detailsUser, name='detailsUser'),
    path('delete/<int:id>/', views.deleteUser, name='deleteUser'),
    path('changeActive/<int:id>/', views.changeActive, name='changeActive'),
    path('manage-users/', views.manageUsers, name='manageUsers'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
