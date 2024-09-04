from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('signUp', views.signUp, name='signUp'),
    path('signIn', views.signIn, name='signIn'),
    path('details/<int:id>/', views.detailsUser, name='detailsUser'),
    path('delete/<int:id>/', views.deleteUser, name='deleteUser'),
    path('changeActive/<int:id>/', views.changeActive, name='changeActive'),
    path('changeAccessAdminPanel/<int:id>/', views.changeAccessAdminPanel, name='changeAccessAdminPanel'),
    path('changeSuperadmin/<int:id>/', views.changeSuperadmin, name='changeSuperadmin'),
    path('changeGroup/<int:id>/<str:group>/', views.changeGroup, name='changeGroup'),
    path('manage-users/', views.manageUsers, name='manageUsers'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
