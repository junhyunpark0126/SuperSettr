# once you make signals.py, you must add the ready method within the apps.py file

from django.db.models.signals import post_save # signal that gets fired after an object is saved
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User) # when a user is saved, send the post_save signal and the receiver (create_profile) will receive it
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs): # instance is the user
    instance.profile.save()