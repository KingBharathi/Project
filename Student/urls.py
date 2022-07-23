from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Home/', views.home, name="home"),
    path('Contact/', views.contact, name="contact"),
]
