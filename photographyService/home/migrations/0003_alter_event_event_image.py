# Generated by Django 4.1.1 on 2022-09-21 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_event_event_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.ImageField(upload_to='event_images'),
        ),
    ]