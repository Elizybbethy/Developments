from django.urls import path

from django.contrib.auth import views as auth_views

from africApp import views

urlpatterns = [
    path('', views.index, name= 'index'),
]
