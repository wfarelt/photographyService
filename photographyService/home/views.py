from django.shortcuts import render, redirect
from .models import Event, Photo, Profile
from django.conf import settings
from datetime import date, timedelta
# Import Strip
import stripe


# Create your views here.

def home(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'home.html', context)

def view_event(request, slug):
    event = Event.objects.filter(slug=slug).first()
    photos = Photo.objects.filter(event=event)
    context = {
        'event': event,
        'photos': photos
    }
    return render(request, 'view_event.html', context)

def become_pro(request):
    if request.method == 'POST':
        membership = request.POST.get('membership','MONTHLY')
        amount = 1
        if membership == 'YEARLY':
            amount = 10
        stripe.api_key = settings.STRIPE_SECRET_KEY

        customer = stripe.Customer.create(
            email=request.user.email,       
            name=request.user.username,
            source=request.POST['stripeToken']
        )
        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*1,
            currency='usd',
            description='Photography Service'
        )
        if charge['paid'] == False:
            profile = Profile.objects.filter(user=request.user).first()
            profile.is_pro = True
            profile.pro_exp_date = date.today() + timedelta(days=30)
            profile.subscription_type = membership
            profile.save()
            return redirect('/charge/')
        
    return render(request, 'become_pro.html')

def charge(request):
    return render(request, 'charge.html')

def photographer(request):
    return render(request, 'photographer.html')

def my_events(request):
    #events = Event.objects.filter(photographer=request.user)
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'my_events.html', context)