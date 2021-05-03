from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Chat(models.Model):
    senderUser=models.ForeignKey(User,related_name="senderUser" ,on_delete=models.CASCADE)
    RecieverUser = models.ForeignKey(User,related_name="recieverUser", on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField( auto_now=True)
    