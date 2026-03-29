from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # NEW FIELD
    name = models.CharField(max_length=100, blank=True)

    bio = models.TextField(blank=True)

    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    
    skills = models.CharField(
        max_length=300,
        blank=True,
        help_text="Enter skills separated by commas (e.g. Python, Django, HTML)"
    )

    def __str__(self):
        return self.user.username
    

from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


    
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()