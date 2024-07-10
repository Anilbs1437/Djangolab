# datetime_app/views.py
from django.shortcuts import render
import datetime

def current_datetime(request):
    X = datetime.datetime.now()
    return render(request, 'datetime_app/current_datetime.html', {'current_datetime': X})
