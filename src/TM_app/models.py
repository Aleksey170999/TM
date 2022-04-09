from django.db import models
from datetime import datetime

class TimesModel(models.Model):
    user_name = models.CharField(max_length=50, blank=False, default='123')

    in_date = models.DateField(blank=False, default=datetime.now)
    out_date = models.DateField(blank=False, default=datetime.now)

    in_time = models.TextField(blank=False)
    out_time = models.TextField(blank=False)
    

    def __str__(self):
        return f'{self.user_name}'
