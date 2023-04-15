from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


#Created an extension for the new user.
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), unique=True, max_length=200)
    email = models.EmailField(_('email address'), unique=True, max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    # The usermanager to mange users.
    objects = CustomUserManager()
    
     #Email is used to Login
    USERNAME_FIELD = 'username'
    
    
    #The required field is the username
    REQUIRED_FIELDS = ['email']
    
    
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

    


#This is the profile of the New user. A profile is formed immediately the user is created.
class Profile(models.Model):
    CHOICES = (
        ('SE', 'Secondary'),
        ('WA', 'Waec'),
        ('JA', 'Jamb'),
        ('UN', 'Undergraduate'),
        ('GR', 'Graduate'),
    )
    OPTIONS = ( 
        ('MA', 'Male'),
        ('FE', 'Female'),
        )
    user = models.OneToOneField('account.User', on_delete=models.CASCADE)
    gender = models.CharField(max_length=250, choices=OPTIONS, blank=True)
    images = models.ImageField(_("image"), upload_to = upload_to, blank=True, null=True)
    level = models.CharField(max_length=100, choices = CHOICES, blank=True)
    coin = models.PositiveBigIntegerField(default=2000)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username


