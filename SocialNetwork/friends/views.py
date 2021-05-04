from django.shortcuts import render
from django.http import HttpResponse
from Users.models import CustomUser 
from .models import FriendRequest
import json
# Create your views here.
def send_friend_request(request):
    user = request.user
    payload={}
    if request.method == "POST" and user.is_authenticated:
        user_id = request.POST.get("reciever_user_id")
        if user_id:
            reciever = CustomUser.objects.get(pk=user_id)
            try:
                friend_requests = FriendRequest.objects.filter(sender=user , reciever=reciever)
                try:
                    for requests in friend_requests:
                       if request.is_active:
                           raise Exception("Friend request already sent")
                    friend_request = FriendRequest(sender=user ,reciever=reciever)
                    friend_request.save()    
                    payload['response']="friend Request sent "   

                except Exception as e:
                    payload['response']= str(e)    

            except FriendRequest.DoesNotExists:
                friend_request = FriendRequest(sender=user , reciever=reciever)  
                friend_request.save()
                payload['response']="friend Request sent "  
            if payload['response'] == None:
                payload['response']="something went wrong"  
        else:
             payload['response']="Unable to send a friend request."      

    else:
        payload['response']="you must login to send a friend request " 
    return HttpResponse(json.dumps(payload) , content_type="application/json")    



