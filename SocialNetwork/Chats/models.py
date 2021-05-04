from django.db import models
from Users.models import CustomUser
# Create your models here.


class Chat(models.Model):
    senderUser = models.ForeignKey(
        CustomUser, related_name="senderUser", on_delete=models.CASCADE)
    RecieverUser = models.ForeignKey(
        CustomUser, related_name="recieverUser", on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
