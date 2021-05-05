

from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import CustomUser, Friend, FriendRequest


@receiver(post_save, sender=FriendRequest)
def post_save_add_to_friends(sender, instance, created, **kwargs):
    sender_ = instance.Sender
    receiver_ = instance.Reciever
    if instance.status == 'accepted':
        sender_.friends.add(receiver_.id)  # field id
        receiver_.friends.add(sender_.id)
        sender_.save()
        receiver_.save()


@receiver(pre_delete, sender=FriendRequest)
def pre_delete_remove_from_friends(sender, instance, **kwargs):
    sender = instance.Sender  # instance from FriendRequetsModel
    receiver = instance.Reciever
    sender.friends.remove(receiver.id)  # custumUser
    receiver.friends.remove(sender.id)
    sender.save()
    receiver.save()
