from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.Government,name="government-home"),
]