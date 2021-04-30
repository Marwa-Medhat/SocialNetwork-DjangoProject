from django.db import models

from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class UserDetails(models.Model):
    user_id=models.ForeignKey(User, related_name="details", on_delete=models.CASCADE);
    gender = models.CharField(choices=[('male', 'male') , ('female' , 'female')], max_length=50);
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    profile_avatar = models.ImageField(upload_to='media/avatars', max_length=50 , default="default.png")
class Friend(models.Model):
    user_id=models.ForeignKey(User, related_name="user", on_delete=models.CASCADE); 
    friend_id =models.ForeignKey(User, related_name="userfriend", on_delete=models.CASCADE); 

class FriendRequest(models.Model):
    Reciever=models.ForeignKey(User, related_name="reciever", on_delete=models.CASCADE); 
    Sender =models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE); 
