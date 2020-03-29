import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jsonexam.settings')
django.setup()

from jsonapp.models import *
from django.contrib.auth.models import User
from django.utils import timezone
from faker import Faker
import random
import string
faker = Faker()

def populate(n):
    for i in range(n):
        f_id = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(8)])
        f_real_name = faker.name()
        f_tz = faker.timezone()
        Users.objects.create(id=f_id,real_name=f_real_name,tz=f_tz)
        for j in range(2):
            f_start_time = faker.date_time(tzinfo=None, end_datetime=None)
            f_end_time = faker.date_time(tzinfo=None, end_datetime=None)
            ActivityPeriod.objects.create(start_time=f_start_time,End_time=f_end_time)

populate(5)
