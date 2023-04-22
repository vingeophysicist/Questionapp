from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.




class Subject(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, max_length=500)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Subject, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Question(models.Model):
    COINS_CHOICES = (
        (10, 10),
        (20, 20),
        (30, 30),
        (40, 40),
        (50, 50),
        (60, 60),
        (70, 70),
        (80, 80),
        (90, 90),
        (100, 100),

    )
    
    label = models.CharField(max_length=5000)
    image = models.ImageField()
    slug = models.SlugField(unique=True, max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coins_given = models.PositiveSmallIntegerField(choices=COINS_CHOICES, blank=False, null=True)
    
    def __str__(self):
        return self.label
    
class Answer(models.Model):
    label = models.CharField(max_length=5000)
    image = models.ImageField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name = "answers")
    clappers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="claps")
    
    
    def __str__(self):
        return self.user.username
    
    
class Comment(models.Model):
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
