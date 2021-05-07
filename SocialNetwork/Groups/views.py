from django.shortcuts import render, redirect, get_object_or_404
from .models import Group
from Posts.models import Post
from Posts.forms import PostsCreateForm
from .forms import GroupsCreateForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from Users.models import CustomUser
# Create your views here.

def index(request):

    groups = Group.objects.all()
    form = GroupsCreateForm()
    # print(form)
    return render(request, "groups/index.html",
                  {
                      "groups": groups,
                      "form": form
                  })


def create(request):
    form = GroupsCreateForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        description = form.cleaned_data.get('description')
        group = Group(name=name , owner=request.user, description=description )
        group.save()
        return redirect("listgroup")

    return render(request, "groups/create.html", {
        "form": form,
    })


def viewGroup(request, id):
    group = Group.objects.get(id=id)
    posts = Post.objects.filter(Group_id=group).order_by('-creation_date_time')
    #print(posts)
    form = PostsCreateForm()
    # print(form)
    return render(request, "groups/group.html",
                  {
                      "group": group,
                      "posts": posts,
                      "form": form
                  })

def groups(request):
    groups = Group.objects.filter(owner_id=request.user.id)
    form = GroupsCreateForm()
    # print(form)
    return render(request, "groups/index.html",
                  {
                      "groups": groups,
                      "form": form
                  })

def groupDetails(request, id):
    group = Group.objects.get(id=id)
    membersCount = group.members.all().count()
    return render(request, "groups/groupdetails.html",
                  {
                      "group": group,
                      "membersCount": membersCount
                    
                  })

def joingroup(request, id):
    group = Group.objects.get(pk=id)
    group.requests.add(request.user)
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def requestsingroup(request, id):
    group = Group.objects.get(pk=id)
    requests = group.requests.all()
    return render(request, "groups/requests.html",
                  {
                      "requests": requests,
                      "group": group    
                  })


def membersingroup(request, id):
    group = Group.objects.get(pk=id)
    members = group.members.all()
    return render(request, "groups/members.html",
                  {
                      "members": members,
                      "group": group    
                  })

def accept(request, groupid, userid):
    group = Group.objects.get(pk=groupid)
    user = CustomUser.objects.get(pk=userid)
    group.members.add(user)
    accepteduser = group.requests.get(username= user.username)
    group.requests.remove(accepteduser)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def decline(request, groupid, userid):
    group = Group.objects.get(pk=groupid)
    user = CustomUser.objects.get(pk=userid)
    declineduser = group.requests.get(username= user.username)
    group.requests.remove(declineduser)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete(request, groupid, userid):
    group = Group.objects.get(pk=groupid)
    user = CustomUser.objects.get(pk=userid)
    declineduser = group.members.get(username= user.username)
    group.members.remove(declineduser)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def deletegroup(request, id):
    Group.objects.get(pk=id).delete()
    
    #Group.remove(group)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



