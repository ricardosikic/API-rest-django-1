from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=100)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=200, default='')
    dob = models.DateField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='uploads', blank=True)


class Article(models.Model):
    photo = models.ImageField(upload_to='uploads', blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title