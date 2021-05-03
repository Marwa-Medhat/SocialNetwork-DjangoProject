from django.db import models
from django.contrib.auth.models import User
from Groups.models import Group 
from datetime import datetime  
from django.utils import timezone   
from django.urls import reverse
class Post(models.Model):
    user_id=models.ForeignKey(User, related_name="userPosts", on_delete=models.CASCADE);
    content = models.TextField()
    creation_date_time = models.DateTimeField(auto_now=True)
    Group_id = models.ForeignKey(Group,related_name="group", on_delete=models.CASCADE , blank=True, null=True)
    post_image = models.ImageField(upload_to='images',null=True,blank=True)
    likes = models.ManyToManyField(User,related_name='post_likes',null=True,blank=True)

    def total_likes(self):  
        return self.likes.count()
    def get_absolute_url(self):
        return reverse('details', kwargs={'id': self.id})


class Comment(models.Model):
    post_id= models.ForeignKey(Post, related_name="post", on_delete=models.CASCADE)
    content = models.TextField(null=True,blank=True)
    creation_date_time = models.DateTimeField(auto_now=True)


class BadWords(models.Model):
    word= models.CharField( max_length=50)



     
