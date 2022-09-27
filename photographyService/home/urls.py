from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view_event/<slug:slug>', views.view_event, name='view_event'),
    path('become_pro', views.become_pro, name='become_pro'),
    path('charge', views.charge, name='charge'),
    path('photographer', views.photographer, name='photographer'),
    path('my_events', views.my_events, name='my_events'),
]