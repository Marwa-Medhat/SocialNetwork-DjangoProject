import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Chat  , rooms
from Users.models import CustomUser , FriendRequest
from django.db.models import Q 
from django.core.mail import EmailMultiAlternatives
from Notifications.models import Notification
from django.core.mail import send_mail
from django.template.loader import render_to_string

class ChatConsumer(WebsocketConsumer):
    def message_to_json(self, message):
     
        return {
            'sender':message.senderUser.username,
            'message':message.content,
            'date':str(message.date),
            'reciever':message.RecieverUser.username
        }         
    def messages_to_json(self , messages):
        result = [];
        for message in messages:
            result.append(self.message_to_json(message));
        return result
    def fetch_messages(self,data):
        user = data['from']
        sender = CustomUser.objects.filter(username=user)[0]
        # Reciver = CustomUser.objects.get(pk=self.room_name)
        room = rooms.objects.get(pk=self.room_name) 
        messages = Chat.last_10_messages(room)
       
        # room = rooms.objects.filter(Q(user1=sender, user2=Reciver) | Q(user1=Reciver, user2=sender)).first()
        # if room :
        #      
        content = {
            'messages' : self.messages_to_json(messages),
            'command':'message'
        }
        self.send_message(content)

     

        
    def new_message(self , data):
        user = data['from']
        sender = CustomUser.objects.filter(username=user)[0]
        # Reciver = CustomUser.objects.get(pk=self.room_name)
        Reciver = ""
        room = rooms.objects.get(pk=self.room_name) 
        if room.user1 == sender:
            Reciver = room.user2
        else:
            Reciver = room.user1    
        room.isread=False
        room.save()    


        message = Chat.objects.create(senderUser=sender,RecieverUser =Reciver, content=data['message'])
        room.room_messages.add(message)

        
     
     
        
        # else http://localhost:8000/chat/3/:
        #    room=rooms.objects.create(user1=sender,user2=Reciver);
        #    room.room_messages.add(message)
        #    room.save()
   


        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        # self.send_email(Reciver.email)
        return self.send_chat_message(content ,  Reciver , sender)
       


    commands={
        'fetch-messages':fetch_messages,
        'new-message':new_message
    }
    def connect(self):   
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # Join room group
     
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
           
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data= json.loads(text_data)
        print(self.room_name)
        self.commands[data['command']](self, data)

    def send_chat_message(self , message , Reciever, sender):    
        # Send message to room group
       
        async_to_sync( self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                
            }
        )
   

    # Receive message from room group
    def chat_message(self, event):
     
      
       message = event['message']
      
     
       self.send(text_data=json.dumps(message))
      
       self.send_email(message)
       
       
    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def send_email(self , message ):
        reciever =    message['message']['reciever']
        sender = message['message']['sender']
        RecieverUser = CustomUser.objects.get(username=reciever)
        senderUser = CustomUser.objects.get(username=sender)
        msg_plain = render_to_string('email/email.txt', {'username': f'{RecieverUser.first_name}{RecieverUser.last_name}' , 'Sender' : f'{senderUser.first_name}{senderUser.last_name}' , 'message' : message['message']['message']})
        msg_html = render_to_string('email/email.html', {'username': f'{RecieverUser.first_name}{RecieverUser.last_name}' , 'Sender' : f'{senderUser.first_name}{senderUser.last_name}' , 'message' : message['message']['message']})
        send_mail(
               'email title',
                msg_plain,
               'onair',
               [RecieverUser.email],
               html_message=msg_html,)


    # =====  ======================================================================================================  # Send message to WebSocket
class NotificationConsumer(WebsocketConsumer):
    def fetch_likes(self):
        pass
    def fetch_messages(self):
        pass
    def fetch_requests(self):
        pass
    def fetch_comments(self):
        print("comment")
    command = {
        'likes': fetch_likes,
        'comment': fetch_comments,
        'requests':fetch_requests,
        'messages':fetch_messages,
    }
    def connect(self):
        self.user_name = self.scope['url_route']['kwargs']['user_name']
        print (self.user_name)
        self.room_group_name = 'chat_%s' % self.user_name
        # Join room group
     
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
           
        )
     

        self.accept()
        # user = CustomUser.objects.get(username=self.user_name)
        # count_messages = Chat.objects.filter(RecieverUser=user).count();
        # count_notification = Notification.objects.filter(RecieverUser=user , seen=False).count(); 
        # count_rooms = rooms.objects.filter(Q(user1=user , isread=False) | Q(user2=user , isread=False)).count();
        # count_friend_request = FriendRequest.objects.filter( Reciever = user , status="send").count()

        # self.send(text_data=json.dumps(
        #     {
        #         'messages' : count_rooms,
        #         'notification' : count_notification,
        #         'requests' : count_friend_request,
                
                
              
        #     }
        # )) 
        print("connected")  
    def receive(self, text_data):
        
        data= json.loads(text_data)
        currentuser = data['currentuser']
        user = CustomUser.objects.get(username=self.user_name)
        count_messages = Chat.objects.filter(RecieverUser=user , isread=False).count();     
        if user.username == data['currentuser']:
           count_rooms = rooms.objects.filter(Q(user1=user , isread=False) | Q(user2=user , isread=False)).count();
        count_notification = Notification.objects.filter(RecieverUser=user , seen=False).count();
        count_friend_request = FriendRequest.objects.filter( Reciever = user , status="send").count()
        self.send(text_data=json.dumps(
            {
                'messages' :  count_messages,
                'notification' : count_notification,
                'requests' : count_friend_request,
                
              
            }
        )) 
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )    