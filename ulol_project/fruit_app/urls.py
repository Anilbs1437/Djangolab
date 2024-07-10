from django.urls import path
from . import views

urlpatterns = [
    path('anil/', views.fruit, name='index'),
]
