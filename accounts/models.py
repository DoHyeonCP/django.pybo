from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Profile(models.Model):
    username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(max_length = 500, blank=True, default="소개글을 작성해보세요")
    profile_pic = models.ImageField(upload_to='profile_pics', blank= True, null= True)