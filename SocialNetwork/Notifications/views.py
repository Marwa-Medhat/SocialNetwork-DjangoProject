from django.shortcuts import render
from.models import Notification
from Users.models import CustomUser
# Create your views here.
def index(request):
       
        notifications = Notification.objects.filter(RecieverUser=request.user)
        for notification in notifications:
          notification.seen=True
          notification.save() 
        return render(request, 'Notifications/notification.html', {
           
          'notifications':notifications
          
    })
    




