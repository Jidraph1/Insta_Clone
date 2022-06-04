from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.
class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=60)
    caption = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='app_user')


class Profile(models.Model):
    profile_photo = CloudinaryField('image')
    bio = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


