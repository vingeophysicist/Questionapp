from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import Profile, User



#The profile is created immediately the user creates a user account.
@receiver(post_save, sender=User)
def create_related_profile(sender, instance, created, *args, **kwargs):
    if instance and created:
        instance.profile = Profile.objects.create(user=instance)