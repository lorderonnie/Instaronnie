from django.db import models
from django.contrib.auth.models import User
from django.utils.datetime_safe import date
import datetime

class Profile(models.Model):
    '''
    this is a model class that defines how a user profile will be created
    '''
    user  = models.OneToOneField(User, on_delete = models.CASCADE, default='')
    profile_pic = models.ImageField(upload_to = 'media/', default='default.jpg')
    bio =models.TextField()
    updated_on = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return f'{self.user.username} profile'
    
    def search_user(cls,username):
        '''
        Function for searching a user
        '''
        found_user = User.objects.get(user= user)

    def save_profile(self):
        '''
        Function for saving a profile
        '''
        self.save()

    @classmethod
    def get_profile_by_name(cls,name):
        '''
        this is a class method that gets a profile by name
        '''
        profile = cls.objects.filter(user = name)

        return  name 
   
class Photos(models.Model):
    picture = models.ImageField(upload_to= 'media/')
    name = models.CharField(max_length=50)
    caption = models.CharField(max_length=300)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes' ,blank=True,)

    @classmethod
    def get_all_photos(cls):
        photos = cls.objects.all()
        return photos

    @classmethod
    def get_photos_by_name(cls,name):
        photos = cls.objects.filter(name= name)
        return photos        
     
    def save_photo(self):
        self.save()

    def delete_photo(self):
        self.delete()   
        
class Comments(models.Model):
    comment = models.CharField(max_length=500)
    posted_by = models.ForeignKey(User, on_delete = models.CASCADE)
    posted_on = models.DateField(auto_now_add=True)
    image_id = models.ForeignKey(Photos,on_delete= models.CASCADE)       
    def __str__(self):
        return self.user

    @classmethod
    def get_all_comments(cls,id):
        comments = cls.objects.filter(picture_id=id)
        return comments

    def save_comments(self):
        self.save()

    def delete_comment(self):
        self.delete()
        
        
        
        
        
        