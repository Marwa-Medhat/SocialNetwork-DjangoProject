from django.shortcuts import render
from.models import Notification
from Users.models import CustomUser
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required() 
def index(request):
       
        notifications = Notification.objects.filter(RecieverUser=request.user).order_by('-date')
        for notification in notifications:
          notification.seen=True
          notification.save() 
        return render(request, 'Notifications/notification.html', {
           
          'notifications':notifications
          
    })
    




