from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import  Chat 
from Users.models import CustomUser
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail
from django.template.loader import render_to_string
@receiver(post_save , sender=Chat)
def after_chat_creation(sender , instance, created, *args, **kwargs):
    if created:
            msg_plain = render_to_string('email/email.txt', {'username': f'{instance.RecieverUser.first_name}{instance.RecieverUser.last_name}' , 'Sender' : f'{instance.senderUser.first_name}{instance.senderUser.last_name}' , 'message' : instance.content})
            msg_html = render_to_string('email/email.html', {'username': f'{instance.RecieverUser.first_name}{instance.RecieverUser.last_name}' , 'Sender' : f'{instance.senderUser.first_name}{instance.senderUser.last_name}' , 'message' : instance.content})
            send_mail(
               'email title',
                msg_plain,
               'onair',
               [instance.RecieverUser.email],
               html_message=msg_html,
)


        
        # subject, from_email, to = 'hello', 'from@example.com', 'to@example.com'
        # text_content = 'This is an important message.'
        # html_content = '<p>This is an <strong>important</strong> message.</p>'
        # msg = EmailMultiAlternatives(subject, html_content, 'lifehotel881@gmail.com', [instance.RecieverUser.email])
        # msg.send() 
        
        

        # isbn_create=ISBN(Author_name=instance.Author.username)
        # isbn_create.save()
        # instance.isbn_number=isbn_create
        # instance.save()