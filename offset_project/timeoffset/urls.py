from django.urls import path
from . import views
urlpatterns = [
path('anil/', views.time_offset_view, name='datetime_offsets'), ]