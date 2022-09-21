from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_description = RichTextField()
    is_premium = models.BooleanField(default=False)
    event_image = models.ImageField(upload_to='event.png')
    slug = models.SlugField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.event_name)
        super(Event, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.event_name

