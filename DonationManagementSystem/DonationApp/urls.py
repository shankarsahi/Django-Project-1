
from django.contrib import admin
from django.urls import path
from DonationApp import views






urlpatterns = [
    path("",views.index),
]

