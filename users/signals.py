import os
from PIL.Image import SAVE
from django.db import models
from django.db.models.signals import post_save, pre_save
from .models import User, profile
from django.dispatch import receiver


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance).save()


@receiver(pre_save, sender=profile)
def deleteProfile(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_avatar = profile.objects.get(pk=instance.pk).image
        except:
            return
        else:
            old_avatar.delete(save=False)
