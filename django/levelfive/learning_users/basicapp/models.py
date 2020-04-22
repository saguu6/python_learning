from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
        #relationship
    user = models.OneToOneField(User)

    #additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic',blank=True)

    def __str__(self):
        return self.user.username   #username is coming from user table
