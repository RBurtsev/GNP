from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Owners(models.Model):
    full_name = models.CharField(max_length=60)
    mail = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    land_adress = models.CharField(max_length=100, default="empty", null=True, blank=True)
    home_adress = models.CharField(max_length=100, default="empty", null=True, blank=True)


class Indicators(models.Model):
    id_owner = models.CharField(max_length=60)
    gas = models.CharField(max_length=60)
    water = models.CharField(max_length=100)
    electric = models.CharField(max_length=100)


class NotOwners(models.Model):
    full_name = models.CharField(max_length=60)
    mail = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    home_adress = models.CharField(max_length=100, default="empty", null=True, blank=True)


class Ads(models.Model):
    IMPORTANT = "Important"
    ORDINARY = "Ordinary"
    TYPE = [
        ('Important', 'Important'),
        ('Ordinary', 'Ordinary')
    ]
    type_ads = models.CharField(
        max_length=9,
        choices=TYPE,
        default=ORDINARY
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)



