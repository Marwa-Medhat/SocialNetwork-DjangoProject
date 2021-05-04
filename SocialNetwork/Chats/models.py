from django.db import models
from Users.models import CustomUser
# Create your models here.


class Chat(models.Model):
    senderUser = models.ForeignKey(
        CustomUser, related_name="senderUser", on_delete=models.CASCADE)
    RecieverUser = models.ForeignKey(
        CustomUser, related_name="recieverUser", on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField( auto_now=True)
class rooms(models.Model):
   room_member=models.ManyToManyField(CustomUser, related_name="members")
   room_messages= models.ManyToManyField(Chat, related_name="messages")  
