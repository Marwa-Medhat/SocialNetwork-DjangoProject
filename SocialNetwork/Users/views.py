from Users.forms import RegistrationForm, AccountAuthenticationForm, profileForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import CustomUser , FriendRequest

# from .models import UserDetails
from .models import CustomUser


# Create your views here.
# profile page
def index(request):
    users = CustomUser.objects.all();
    # # sent_requests = FriendRequest.objects.get(Sender_id=request.user.id)
    # print(sent_requests)
    return render(request, 'Users/listUsers.html',
    {
        'users': users,
        
    } )

def profile(request):
    return render(request, 'Users/profile.html')
def userprofile(request , id):
    user = CustomUser.objects.get(pk=id);
    return render(request, 'Users/userprofile.html' , 
    {
        'user':user
    })
def friendRequest(request , id):
    recieverUser = CustomUser.objects.get(pk=id);
    friend= FriendRequest(Reciever=recieverUser, Sender=request.user)
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
    user = CustomUser.objects.get(id=request.user.id)
    form = profileForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect("profile")
    return render(request, "Users/edit.html", {"form": form, "user": user})

