from django.test import TestCase
from .models import Image, Comment, Profile, Like


# Create your tests here.
class ImageTestCase(TestCase):
    #SetUp Method

    def setUp(self):
        self.Pic = Image(id = '1', image ='example.jpg', name = 'James', caption = 'Same Script different characters', user = 'James', location= 'Juja')

    def test_instance(self):
        self.assertTrue(isinstance(self.Pic, Image))  
        
    def test_save_method(self):
        self.Pic.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_method(self):
        self.Pic.delete_image()
        images = Image.objects.all()
        self.assetTrue(len(images)==0)
        

class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Prof= Profile(id = '1', profile_photo = 'example.jpg', bio = 'Hi there', user ='James')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Prof,Profile)) 
    
     # Testing Save Method
    def test_save_method(self):
        self.Prof.save_profile()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0) 
        
    def test_delete_method(self):
        self.Prof.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)==0)     