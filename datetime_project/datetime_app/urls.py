# datetime_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("anil/", views.current_datetime, name='current_datetime'),
]
