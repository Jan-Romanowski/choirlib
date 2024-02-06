from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('managers', views.managers, name='managers'),
    path('news', views.news, name='news'),
    path('conductor', views.conductor, name='conductor'),
    path('viceConductor', views.viceConductor, name='viceConductor'),
    path('hoffman', views.hoffman, name='hoffman'),
    path('history', views.history, name='history'),
    path('contact', views.contact, name='contact'),
]
