from datetime import date
from django.db import models
from django.contrib.auth import authenticate
import datetime

class TimesModel(models.Model):
    user_name = models.CharField(max_length=50, default='User')
    date = models.DateField(blank=False)
    in_time = models.TextField(blank=False)
    out_time = models.TextField(blank=False)

    def __str__(self):
        return str(self.in_time)
