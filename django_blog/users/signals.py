from django.db.models.signals import post_save
from django.contrib.auth.models import User # Sender
from django.dispatch import receiver 
from .models import Profile


# This will be trigered everytime user are created (Django-Signal)
@receiver(post_save, sender=User) # When a user is saved send this signal to receiver
def create_profile(sender, instance, created, **kwargs): # This function itself is the Receiver
    if created:
        Profile.objects.create(user=instance)

# This will be trigered everytime user is saved
@receiver(post_save, sender=User) 
def save_profile(sender, instance, **kwargs):
    instance.profile.save()