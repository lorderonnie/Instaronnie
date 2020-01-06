from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='media/')
    bio = models.CharField(max_length=300)
    username = models.CharField(max_length=50,default='Your username')

    def __str__(self):
        return self.username

    def search_user(self,cls,username):
        found_user = User.objects.get(username = username)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
        
    @property
    def all_likes(self):
        return self.likes.count()   
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
        photos = cls.objects.filter(posted_by= name)
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