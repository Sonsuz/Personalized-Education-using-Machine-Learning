from django.contrib.auth.models import Permission, User
from django.db import models
import datetime



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lan_ID = models.CharField(max_length=10)
    phone = models.IntegerField(default=0)
    title = models.CharField(max_length=30, default="Title")
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return str(self.user.first_name)
