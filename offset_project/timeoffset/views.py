from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta

def time_offset_view(request):
    current_time = timezone.now()
    time_ahead = current_time + timedelta(hours=4)
    time_before = current_time - timedelta(hours=4)

    context = {
        'current_time': current_time,
        'time_ahead': time_ahead,
        'time_before': time_before,
    }
    
    return render(request, 'timeoffset/time.html', context)
