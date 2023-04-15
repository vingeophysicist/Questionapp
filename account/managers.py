from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _



class CustomUserManager(BaseUserManager):
        
        def _create_user(self, username, email, password, **extra_fields):
             """Create and return a `User` with an email, username and password."""
             if username is None:
                 raise TypeError('Users must have a username.')
             if email is None:
                 raise TypeError('Users must have an email.')
             user = self.model(username=username, email=self.normalize_email(email), **extra_fields)
             user.set_password(password)
             user.full_clean()
             user.save()
             return user
        
        def create_user(self, username, email, password, **extra_fields):
            extra_fields.setdefault("is_staff", False)
            extra_fields.setdefault("is_superuser", False)
            return self._create_user(username, email, password, **extra_fields)
        
        def create_superuser(self, username, email, password, **extra_fields):
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)   
            
            if extra_fields.get('is_staff') is not True:
                raise ValueError('superuser must have staff previledge')
            return self._create_user(username, email, password, **extra_fields)