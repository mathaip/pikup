from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.shortcuts import render, redirect

urlpatterns =[
path('', views.landing, name="landing"),
path('register', views.register, name='register'),
path('login', views.login, name="login"),
path('passenger/profile', views.pprofile, name = 'passenger profile page')

]