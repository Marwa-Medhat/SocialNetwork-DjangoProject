from Users.forms import RegistrationForm, AccountAuthenticationForm, profileForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
# from .models import UserDetails
from .models import CustomUser


# Create your views here.
# profile page
def index(request):
    return render(request, 'Users/profile.html')


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
    user = CustomUser.objects.get(pk=id)
    form = profileForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect("login")
    # return render(request, "Users/edit.html", {"form": form, "user": user})
    return HttpResponseRedirect(request, "Users/edit.html", {"form": form, "user": user})
