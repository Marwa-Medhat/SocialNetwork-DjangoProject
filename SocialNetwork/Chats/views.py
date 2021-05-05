from django.shortcuts import render
from django.db.models import Q
from.models import rooms
# Create your views here.
def index(request):
    return render(request, 'chat/index.html', {})  

def room(request, room_name):
    userrooms= rooms.objects.filter(Q(user1=request.user) | Q(user2=request.user))
    
    return render(request, 'chat.html', {
        'room_name': room_name,
        'username':request.user.username,
        'rooms' : userrooms
    })