from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from home.models import Profile

# Create your views here.

class SignUp(generic.CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    form_class = UserCreationForm

def profile(request):
    profile = Profile.objects.get(user=request.user)
    context = {
        'user': request.user,
        'profile': profile
    }
    return render(request, 'registration/profile.html', context)
