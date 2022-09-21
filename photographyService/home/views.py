from django.shortcuts import render
from .models import Event
# Create your views here.

def home(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'home.html', context)