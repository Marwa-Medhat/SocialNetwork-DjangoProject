from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import  Chat 
from Users.models import CustomUser
@receiver(post_save , sender=Chat)
def after_book_creation(sender , instance, created, *args, **kwargs):
    if created:
        user = CustomUser.objects.get(pk=instance.RecieverUser.id)
        

        # isbn_create=ISBN(Author_name=instance.Author.username)
        # isbn_create.save()
        # instance.isbn_number=isbn_create
        # instance.save()