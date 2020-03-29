from django.db import models


# Create your models here.
class Users(models.Model):
    import pytz
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    id = models.CharField(max_length=20,primary_key=True)
    real_name = models.CharField(max_length=30)
    tz = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')

class ActivityPeriod(models.Model):
    start_time = models.DateField(auto_now=True)
    End_time = models.DateField(auto_now=True)
