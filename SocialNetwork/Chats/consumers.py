import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Chat  , rooms
from Users.models import CustomUser
from django.db.models import Q

class ChatConsumer(WebsocketConsumer):
    def message_to_json(self, message):
        return {
            'sender':message.senderUser.username,
            'message':message.content,
            'date':str(message.date)
        }         
    def messages_to_json(self , messages):
        result = [];
        for message in messages:
            result.append(self.message_to_json(message));
        return result
    def fetch_messages(self,data):
        user = data['from']
        sender = CustomUser.objects.filter(username=user)[0]
        Reciver = CustomUser.objects.get(pk=self.room_name)
        
        room = rooms.objects.filter(Q(user1=sender, user2=Reciver) | Q(user1=Reciver, user2=sender)).first()
        if room :
            room.room_messages.add(message)
        else :
           room=rooms.objects.create(user1=sender,user2=Reciver);
           room.room_messages.add(message)
           room.save()
        messages = Chat.last_10_messages()
        content = {
            'messages' : self.messages_to_json(messages),
            'command':'message'
        }
        self.send_message(content)

     

        
    def new_message(self , data):
        user = data['from']
        sender = CustomUser.objects.filter(username=user)[0]
        Reciver = CustomUser.objects.get(pk=self.room_name)
        message = Chat.objects.create(senderUser=sender,RecieverUser =Reciver, content=data['message'])
        room = rooms.objects.filter(Q(user1=sender, user2=Reciver) | Q(user1=Reciver, user2=sender)).first()
        if room :
            room.room_messages.add(message)
        else :
           room=rooms.objects.create(user1=sender,user2=Reciver);
           room.room_messages.add(message)
           room.save()

        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        return self.send_chat_message(content)
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

    def send_chat_message(self , message):    
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
       
    def send_message(self, message):
        self.send(text_data=json.dumps(message))


        # Send message to WebSocket
class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        count_messages = Chat.objects.all().count();
       

        self.send(text_data=json.dumps(
            {
                'messages' : count_messages,
              
            }
        )) 
        print("connected")  