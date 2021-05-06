from django.shortcuts import render, redirect, get_object_or_404
from .models import Group
from Posts.models import Post
from Posts.forms import PostsCreateForm
from .forms import GroupsCreateForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
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
        group = Group(name=name , owner=request.user )
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
