import main.views as views

from django.urls import path

urlpatterns = [
    path('', views.index),
]
