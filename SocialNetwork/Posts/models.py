from django.db import models
from Users.models import CustomUser
from Groups.models import Group
# Create your models here.


class Post(models.Model):
    user_id = models.ForeignKey(
        CustomUser, related_name="userPosts", on_delete=models.CASCADE)
    content = models.TextField()
    creation_date_time = models.DateField(auto_now=True)
    Group_id = models.ForeignKey(
        Group, related_name="group", on_delete=models.CASCADE, blank=True, null=True)
    post_image = models.ImageField(
        upload_to='images/', max_length=50, blank=True, null=True)
    likes = models.ManyToManyField(
        CustomUser, related_name='post_likes', null=True, blank=True)

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post_id = models.ForeignKey(
        Post, related_name="post", on_delete=models.CASCADE)
    content = models.TextField()
    creation_date_time = models.DateTimeField(auto_now=True)


# class Likes(models.Model):
#     post_id = models.ForeignKey(
#         Post, related_name="Likedpost", on_delete=models.CASCADE)
#     user_id = models.ForeignKey(
#         CustomUser, related_name="likedUser", on_delete=models.CASCADE)


class BadWords(models.Model):
    word = models.CharField(max_length=50)
