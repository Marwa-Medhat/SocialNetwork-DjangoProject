from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'chat/index.html', {})  

def room(request, room_name):
    print(room_name)
    return render(request, 'chat.html', {
        'room_name': room_name,
        'username':request.user.username
})