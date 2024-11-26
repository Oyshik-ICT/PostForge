from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Automatically create a Profile when a new User is created.
    """
    try:
        if created:
            Profile.objects.create(user=instance)
    except Exception as e:
        print(f"Error creating profile for user {instance.username}: {e}")


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Automatically save the associated Profile when User is saved.
    """
    try:
        instance.profile.save()
    except Exception as e:
        print(f"Error saving profile for user {instance.username}: {e}")
