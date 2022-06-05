from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.
class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=60)
    caption = models.CharField(max_length=250)
    user = models.ForeignKey(User,on_delete = models.CASCADE, related_name='app_user')
    posted_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.name
    
    ordering = ['-posted_at']
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
     
    @classmethod
    def all_images(cls):
        images = cls.objects.filter().order_by('-posted_at')
        return images  
         
    @classmethod
    def search_image(cls,search_term):
        """
    A method that searches an image
     """
        images = cls.objects.filter(name__icontains=search_term)
        return images  

    



class Profile(models.Model):
    profile_photo = CloudinaryField('image')
    bio = models.CharField(max_length=250)
    user = models.OneToOneField(User,on_delete = models.CASCADE)

    def __str__(self):
        return self.user
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()    

    @classmethod
    def search_profile(cls,search_term):
        profiles = cls.objects.filter(user__username__icontains = search_term).all()
        return profiles    


class Like(models.Model):
    image =models.ForeignKey(Image, on_delete = models.CASCADE,related_name='imagelikes')
    liker=models.ForeignKey(User,on_delete = models.CASCADE,related_name='userlike')    
    
class Comment(models.Model):
    comment = models.CharField(max_length=250)
    image = models.ForeignKey(Image,on_delete = models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='comments')
