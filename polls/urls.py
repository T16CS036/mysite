'''
Created on 2018/10/17

@author: t16cs036
'''
from django.urls import include,path
from django.contrib import admin
from . import views

urlpattern = [
    path('',views.index, name='index'),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls)
    ]