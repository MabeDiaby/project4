from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    profile_pic = models.URLField(max_length=250, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

# class MyUser(AbstractUser):
#     def set_password(self, raw_password):
#         AbstractUser.set_password(raw_password)
#         print('raw_password =', raw_password)