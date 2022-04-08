from django.db import models
from django.contrib.auth import authenticate
from datetime import datetime

class TimesModel(models.Model):
    user_name = models.CharField(max_length=50)

    in_date = models.DateField(blank=False)
    out_date = models.DateField(blank=False)

    in_time = models.TextField(blank=False)
    out_time = models.TextField(blank=False)
    
    pere = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.user_name}____{self.pere}'
