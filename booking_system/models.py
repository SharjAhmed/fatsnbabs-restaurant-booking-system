from django.db import models
from django.contrib.auth.models import User
import datetime


TIME_CHOICES = [
    ("10:00", "10:00"),
    ("10:30", "10:30"),
    ("11:00", '11:00'),
    ("11:30", "11:30"),
    ("12:00", '12:00'),
    ("12:30", "12:30"),
    ("13:00", "13:00"),
    ("13:30", "13:30"),
    ("14:00", "14:00"),
    ("14:30", "14:30"),
    ("15:00", '15:00'),
    ("15:30", "15:30"),
    ("16:00", "16:00"),
    ("16:30", "16:30"),
    ("17:00", "17:00"),
    ("17:30", "17:30"),]


class Table(models.Model):
    number_of_seats = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f'Table #{self.id}, for {self.number_of_seats} people'


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurant_booking')
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False, blank=False)
    time = models.CharField(null=True, blank=False, choices=TIME_CHOICES, max_length=25)

    class Meta:
        unique_together = ["table", "date", "time"]

    def __str__(self):
        return f'{self.date}'
