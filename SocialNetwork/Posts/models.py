from django.db import models
from django.contrib.auth.models import User
from Groups.models import Group 
# Create your models here.
class Post(models.Model):
        user_id=models.ForeignKey(User, related_name="userPosts", on_delete=models.CASCADE);
        content = models.TextField()
        creation_date = models.DateField(auto_now=True)
        Group_id = models.ForeignKey(Group,related_name="group", on_delete=models.CASCADE , blank=True, null=True)
        post_image = models.ImageField(upload_to='media/images', max_length=50 ,blank=True, null=True)
        

class Comment(models.Model):
    post_id= models.ForeignKey(Post, related_name="post", on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateField(auto_now=True)

class Likes(models.Model):
     post_id= models.ForeignKey(Post, related_name="Likedpost", on_delete=models.CASCADE)
     user_id = models.ForeignKey(User, related_name="likedUser", on_delete=models.CASCADE);
class BadWords(models.Model):
    word= models.CharField( max_length=50)
