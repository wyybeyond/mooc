# encoding:utf-8
__author__ = 'wyybeyond'
__date__ = '2018/2/22 15:16'

from users.views import login
from django.urls import path

path('login/', login, name='login')
