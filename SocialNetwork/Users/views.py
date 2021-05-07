from Users.forms import RegistrationForm, AccountAuthenticationForm, profileForm
from Posts.models import Post, Comment
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import CustomUser, FriendRequest 
from django.http import HttpResponse, HttpResponseNotFound
# from .models import UserDetails
from .models import CustomUser, Friend
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q


# Create your views here.
# profile page
# @login_required()
def index(request):
    Reciever = []
    Sender=[]
    friends =[]
    users = CustomUser.objects.all()
    userfriends= Friend.objects.filter(Q(user1=request.user) | Q(user2=request.user))
    sent_requests = FriendRequest.objects.filter(Sender=request.user , status = "send")
    Recieverd_requests = FriendRequest.objects.filter(Reciever =request.user , status = "send")
    for requestall in sent_requests.iterator():
        Reciever.append(requestall.Reciever.id)
    for recievedRequest in  Recieverd_requests:
        Sender.append(recievedRequest.id)
    for friend in  userfriends:
        friends.append(friend.user1.id)
        friends.append(friend.user2.id)





    #     Reciever.append(request. Reciever.username)

    print("-------------------------------------------")
    print( Reciever)
    print("-------------------------------------------")
    return render(request, 'Users/listUsers.html',
                  {
                      'users': users,
                      'sended':Reciever,
                      'recieved': Sender,
                      'friends': friends
                    
                  })

# @login_required()
def profile(request):
    posts = Post.objects.order_by('-creation_date_time')
    print(posts)
    return render(request, 'Users/profile.html',
                  {
                      "posts": posts,
                  })


def userprofile(request, id):
    user = CustomUser.objects.get(pk=id) #al user lma bdos 3la click
    # user1 = CustomUser.objects.get(pk=request.user.id)
    # print(user1) ##al user 2li da5l
    # findfriend = []
    # friends = Friend.objects.all()
    # for friend in friends:
    #     if request.user.username == friend.user1.username: # lw al user 2li da5l howa howa al sender
    #         print(friend.user2)
    #         findfriend.append(friend.user2) #yb2a dol as7abo 

    findfriend = Friend.objects.filter(
    Q(user1=request.user , user2 =user ) | Q(user2=request.user , user1=user))
    posts = Post.objects.all()
    return render(request, 'Users/userprofile.html',
                  {
                      'user': user,
                      "posts": posts,
                      "friends":findfriend,
                  })


def friendRequest(request, id):
    recieverUser = CustomUser.objects.get(pk=id)
    friend = FriendRequest(Reciever=recieverUser, Sender=request.user)
    friend.save()
    return redirect("listusers")


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account,
                  backend='django.contrib.auth.backends.ModelBackend')
            return redirect('index')  # profile
        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'Users/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')  # should redirect to home page


def login_view(request):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("index")  # wall page not profile

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("index")

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    # print(form)
    return render(request, "Users/login.html", context)


def editprofile(request, id):
    # def editprofile(request):
    # user = CustomUser.objects.get(pk=id)
    # form = profileForm(request.POST or None, instance=user)
    user = CustomUser.objects.get(id=request.user.id)
    form = profileForm(request.POST or None,
                       request.FILES or None, instance=user)
    confirm = False
    if form.is_valid():
        form.save()
        confirm = True
        print(form)
        return redirect("profile")
    return render(request, "Users/edit.html", {"form": form, "user": user, "confirm": confirm})
    # return HttpResponseRedirect(request, "Users/edit.html", {"form": form, "user": user})


def invites_received_view(request):
    profile = CustomUser.objects.get(id=request.user.id)
    qs = FriendRequest.objects.invatations_received(profile)
    results = list(map(lambda x: x.Sender, qs))
    is_empty = False
    if len(results) == 0:
        is_empty = True

    context = {
        # 'qs': qs,
        'qs': results,
        'is_empty': is_empty,
    }

    return render(request, 'Users/my_invites.html', context)


def accept_invatation(request):
    if request.method == "POST":
        pk = request.POST.get('profile_pk')
        sender = CustomUser.objects.get(pk=pk)
        receiver = CustomUser.objects.get(username=request.user.username)
        rel = get_object_or_404(
            FriendRequest, Sender=sender,  Reciever=receiver)
        if rel.status == 'send':
            rel.status = 'accepted'
            rel.save()
    return redirect('my-invites-view')


def reject_invatation(request):
    if request.method == "POST":
        pk = request.POST.get('profile_pk')
        print(request.user.username)
        receiver = CustomUser.objects.get(username=request.user.username)
        sender = CustomUser.objects.get(pk=pk)
        rel = get_object_or_404(
            FriendRequest, Sender=sender,  Reciever=receiver)
        rel.delete()
    return redirect('my-invites-view')


def send_invatation(request):
    if request.method == 'POST':
        pk = request.POST.get('profile_pk')
        sender = CustomUser.objects.get(username=request.user.username)
        receiver = CustomUser.objects.get(pk=pk)
        rel = FriendRequest.objects.create(
            Sender=sender,  Reciever=receiver, status='send')

        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profile')


def friendslist(request):
    friends = Friend.objects.filter(
    Q(user1=request.user) | Q(user2=request.user))
    return render(request, 'Users/friendslist.html', {'friends': friends})
    # return HttpResponse('<h1>Page was found</h1>')


def cancelFriendrequest(request):
    if request.method=='POST':
        pk = request.POST.get('profile_pk')
        user = request.user
        sender = CustomUser.objects.get(username=request.user.username)
        receiver = CustomUser.objects.get(pk=pk)

        rel = FriendRequest.objects.get(
            (Q(Sender=sender) & Q(Reciever=receiver)) | (Q(Sender=receiver) & Q(Reciever=sender))
        )
        rel.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profile')

def RemoveFriend(request):
    if request.method=='POST':
        pk = request.POST.get('profile_pk')
        user = request.user
        sender = CustomUser.objects.get(username=request.user.username)
        receiver = CustomUser.objects.get(pk=pk)

        rel = FriendRequest.objects.get(
            (Q(Sender=sender) & Q(Reciever=receiver)) | (Q(Sender=receiver) & Q(Reciever=sender))
        )
        rel.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profile')
       
