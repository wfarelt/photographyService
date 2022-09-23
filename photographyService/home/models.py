from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

SUBSCRIPTION_TYPE = (
    ('F', 'FREE'),
    ('M', 'MONTHLY'),
    ('Y', 'YEARLY')
)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_pro = models.BooleanField(default=False)
    pro_exp_date = models.DateField(null=True, blank=True)
    subscription_type = models.CharField(max_length=20, choices=SUBSCRIPTION_TYPE, default='FREE')

    def __str__(self):
        return self.user.username

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_description = RichTextField()
    is_premium = models.BooleanField(default=False)
    event_image = models.ImageField(upload_to='event_images')
    slug = models.SlugField(blank=True, null=True)
    event_date = models.DateField(default=date.today)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.event_name)
        super(Event, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.event_name

class Photo(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    photo_url = models.URLField(max_length=300)
    can_view = models.BooleanField(default=False)

    def __str__(self):
        return self.photo_url

