# Generated by Django 3.2.20 on 2023-07-26 20:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking_system', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Booking',
            new_name='Reservation',
        ),
    ]
