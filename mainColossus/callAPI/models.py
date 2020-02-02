from django.db import models

# Create your models here.


class Birth_Data(models.Model):
    name = models.TextField(max_length=2000)
    date_birth = models.TextField(max_length=2000)
    place = models.TextField(max_length=2000)
    timeZone = models.TextField(max_length=2000)
