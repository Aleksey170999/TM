from django.db import models
from django.contrib.auth import authenticate


class TimesModel(models.Model):
    user_name = models.CharField(max_length=50, default='SOME STRING')
    in_time = models.DateTimeField(blank=False)
    out_time = models.DateTimeField(blank=False)

    def __str__(self):
        return str(self.in_time)
