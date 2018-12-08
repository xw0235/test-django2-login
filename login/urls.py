#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/10/15 22:09 
# @Author : Aries 
# @Site :  
# @File : urls.py 
# @Software: PyCharm

from django.urls import path
from . import views

app_name = "login"

urlpatterns = [
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout')
]