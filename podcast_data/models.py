from django.db import models

import datetime

from django.db import models
from django.utils import timezone


class Avalanche_Accident(models.Model):
    avalanche_number = models.IntegerField(default=9999)
    url = models.CharField(max_length=1000, default='INPUT URL')
    location = models.CharField(max_length=1000, default='INPUT NAME')
    state = models.CharField(max_length=100, default='INPUT STATE')
    date = models.CharField(max_length=100, default='INPUT DATE')
    summary_description = models.CharField(max_length=1000, default='INPUT SUMMARY DESCRIPTION')
    primary_activity = models.CharField(max_length=1000, default='INPUT NAME')
    primary_travel_mode = models.CharField(max_length=1000, default='INPUT NAME')
    location_setting = models.CharField(max_length=1000, default='INPUT NAME')
    killed = models.IntegerField(default = 9999)
    type = models.CharField(max_length=1000, default='INPUT NAME')
    latitude = models.DecimalField(max_digits=50, decimal_places=12, default=9999)
    longitude = models.DecimalField(max_digits=50, decimal_places=12, default=9999)
    html = models.CharField(max_length=100000, default='INPUT HTML')
    audio_url = models.CharField(max_length=2000, default='INPUT AUDIO URL')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.Name
