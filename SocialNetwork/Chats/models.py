from django.db import models
from Users.models import CustomUser
from django.db.models import Q
# Create your models here.


class Chat(models.Model):
    senderUser = models.ForeignKey(
        CustomUser, related_name="senderUser", on_delete=models.CASCADE)
    RecieverUser = models.ForeignKey(
        CustomUser, related_name="recieverUser", on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField( auto_now=True)
    isread = models.BooleanField(default=False)


    def last_10_messages(room):
        return room.room_messages.all()
    def __str__(self):
        return self.senderUser.username
  
class rooms(models.Model):
    user1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE , related_name="user1")
    user2 = models.ForeignKey(CustomUser, on_delete=models.CASCADE , related_name="user2")
    room_messages= models.ManyToManyField(Chat, related_name="messages") 
    class Meta:
        unique_together = (('user1', 'user2'), ('user2', 'user1'))

        
   
 
    # def roomExists(self , u1 , u2):
    #      room =  self.room_member.objects.filter(Q(user1=u1, user2=u2) | Q(user1=u2, user2=u1)).first()
  

         
