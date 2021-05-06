from django.shortcuts import render
from django.db.models import Q
from.models import rooms
from Users.models import CustomUser
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required() 
def index(request):
       
        userrooms= rooms.objects.filter(Q(user1=request.user) | Q(user2=request.user))
        for room in userrooms :
            room.isread =True
            room.save()
        return render(request, 'chat.html', {
           
           'username':request.user.username,
           'rooms' : userrooms,
          
    })
    

@login_required() 
def room(request, user_id):
        
        room_name=""
        userrooms= rooms.objects.filter(Q(user1=request.user) | Q(user2=request.user))
        sender = CustomUser.objects.filter(username=request.user.username)[0]
        Reciver = CustomUser.objects.get(pk=user_id)
        room = rooms.objects.filter(Q(user1=sender, user2=Reciver) | Q(user1=Reciver, user2=sender)).first()
        if room :
            room_name=room.id;
        else :
            room=rooms.objects.create(user1=sender,user2=Reciver);
            room.save()
            room_name =room.id;
         
        return render(request, 'chat.html', {
           'room_name': room_name,
           'username':request.user.username,
           'rooms' : userrooms,
           'roomdetail': room
    })



