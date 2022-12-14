# Generated by Django 4.1.1 on 2022-09-28 16:44

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('event_description', ckeditor.fields.RichTextField()),
                ('is_premium', models.BooleanField(default=False)),
                ('event_image', models.ImageField(upload_to='event_images')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('event_date', models.DateField(default=datetime.date.today)),
                ('qr_code', models.ImageField(blank=True, upload_to='qr_codes')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_pro', models.BooleanField(default=False)),
                ('pro_exp_date', models.DateField(blank=True, null=True)),
                ('subscription_type', models.CharField(choices=[('F', 'FREE'), ('M', 'MONTHLY'), ('Y', 'YEARLY')], default='FREE', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.ImageField(upload_to='events/images/')),
                ('thumbnail_photo', models.ImageField(blank=True, null=True, upload_to='events/images/thumb/')),
                ('can_view', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.event')),
            ],
        ),
    ]
