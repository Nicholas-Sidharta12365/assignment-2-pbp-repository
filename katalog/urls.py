from django.contrib import admin
from django.urls import path, include
from . import views
# TODO: Implement Routings Here

urlpatterns= {
   path('', views.katalog, name="katalog") 
}