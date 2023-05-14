from django.db import models
from django.conf import settings
from django.utils import timezone
from questionapp.models import Comment
from django.utils.text import slugify





# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=250, default='default-slug', unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name


class Post(models.Model):
    
    
    
    class PostObjects(models.Manager):
        def get_query(self):
            return super().get_queryset().filter(status="published")
    
    options = (
       ("draft", "Draft"),
       ("published", "Published")
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date="published")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=options, default="published")
    objects = models.Manager() #default manager
    PostObjects = models.Manager() # custom manager
    
    class Meta:
        ordering = ("-published",)
    
    def __str__(self):
        return self.title
    
    
    
    