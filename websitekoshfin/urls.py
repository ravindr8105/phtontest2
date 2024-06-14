from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('PrivacyPolicy', views.PrivacyPolicy, name='PrivacyPolicy'),
    # path('applyforloan', views.applyforloan, name='applyforloan'),
    
]
