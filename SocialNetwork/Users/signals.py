

from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import CustomUser, Friend, FriendRequest


@receiver(post_save, sender=FriendRequest)
def post_save_add_to_friends(sender, instance, created, **kwargs):
    # if created:
    if instance.status == 'accepted':
        friend = Friend.objects.create(
            user1=instance.Sender, user2=instance.Reciever)
# friend.add(instance.Reciever)
# sender_ = instance.Sender
# receiver_ = instance.Reciever
# # if instance.status == 'accepted':
# sender_.friends.add(receiver_)  # field id
# receiver_.friends.add(sender_)
# sender_.save()
# receiver_.save()


@receiver(pre_delete, sender=FriendRequest)
def pre_delete_remove_from_friends(sender, instance, **kwargs):
    friend = Friend.objects.filter(
        user1=instance.Sender, user2=instance.Reciever)
    # sender = instance.Sender  # instance from FriendRequetsModel
    # receiver = instance.Reciever
    # sender.friends.remove(receiver.id)  # custumUser
    # receiver.friends.remove(sender.id)
    # sender.save()
    friend.delete()
