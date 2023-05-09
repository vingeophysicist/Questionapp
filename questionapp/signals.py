from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Question
from questionapp.utils import generate_string



@receiver(pre_save, sender=Question)
def add_slug_to_the_question(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.label)
        random_string = generate_string()
        instance.slug = slug + "_" + random_string
    




