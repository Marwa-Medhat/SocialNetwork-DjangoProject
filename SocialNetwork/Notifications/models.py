from django.db import models
from Users.models import CustomUser
from Posts.models import Post
class Notification(models.Model):
    senderUser = models.ForeignKey(
        CustomUser, related_name="NotificationSender", on_delete=models.CASCADE)
    RecieverUser = models.ForeignKey(
        CustomUser, related_name="NotificationReciever", on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField( auto_now=True)
    seen = models.BooleanField(default=False)