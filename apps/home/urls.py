# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('addmonitor/', views.showaddmonitor, name='showaddmonitor'),
    path('history/', views.history, name='history'),
    path('monitors/', views.monitor, name='monitors'),
    path('feedback/', views.showfeedback, name='showfeedback'),
    path('devices/', views.device, name='devices'),
    path('feedback/feedback', views.feedback, name='feedback'),

    # Matches any html file
    path('addmonitor/addmonitor', views.addmonitor, name='addmonitor'),
    path('history/delete/<int:id>/',views.deleteairquality,name="deleteairquality"),
    path('monitors/delete/<int:id>/',views.deletemonitor,name="deletemonitor"),
    path('monitors/edit/<int:id>/',views.showeditmonitor,name="showeditmonitor"),
    path('monitors/editmonitor/edit/<int:id>/',views.editmonitor,name="editmonitor"),
    path('devices/delete/<int:id>/',views.deletedevice,name="deletedevice"),
    path('devices/edit/<int:id>/',views.showeditdevice,name="showeditdevice"),
    path('devices/editdevice/edit/<int:id>/',views.editdevice,name="editdevice"),
]
