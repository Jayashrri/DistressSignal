from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import uuid

# Create your models here.

class Location(models.Model):
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    distress = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):
    instance.Profile.save()

class Tracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uid = models.CharField(default=uuid.uuid1(), max_length=100, blank=False, null=False)

