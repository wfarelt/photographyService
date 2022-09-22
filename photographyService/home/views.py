from django.shortcuts import render
from .models import Event, Photo
# Create your views here.

def home(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'home.html', context)

def view_event(request, slug):
    event = Event.objects.filter(slug=slug).first()
    photo = Photo.objects.filter(event=event)
    context = {
        'event': event,
        'photo': photo
    }
    return render(request, 'view_event.html', context)

def become_pro(request):
    return render(request, 'become_pro.html')