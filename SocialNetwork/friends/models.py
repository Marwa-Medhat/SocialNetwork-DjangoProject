from django.db import models
from Users.models import CustomUser

# Create your models here.
class FriendList(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE , related_name="userfriendowner")
    friends = models.ManyToManyField(CustomUser, related_name="friendListowner" , blank=True, null=True)
    def addFriend(self , account):
        if not account in self.friends.all():
            self.friends.add(account)
    def remove_friend(self , account):
        if account in self.friends.all():
            self.friends.remove(account)       
    def unfriend(self , removee):
        remover_friend  = self
        remover_friend.remove_friend(removee)
        friend_list = FriendList.objects.get(user=removee)
class FriendRequest(models.Model):
    sender = models.ForeignKey(CustomUser, related_name="senderuser", on_delete=models.CASCADE)     
    reciever = models.ForeignKey(CustomUser, related_name="reciveruser", on_delete=models.CASCADE)  
    is_active = models.BooleanField(blank=True, null=False , default=True )  
    timestamp = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.sender.username
    def accept(self):
        reciever_friend_list = FriendList.objects.get(user=self.reciever)
        if  reciever_friend_list :
            reciever_friend_list.addFriend(self.sender)
            sender_friend_list = FriendList.objects.get(user=self.sender)
            if  sender_friend_list :
                reciever_friend_list.addFriend(self.reciever)
                self.is_active=False
                self.save()
    def decline(self):
        self.is_active=False
        self.save()
    def cancel(self):
        self.is_active=False    



    