from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from .forms import PostsCreateForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    posts= Post.objects.order_by('-creation_date_time')
    #print(posts)
    form = PostsCreateForm()
    return render(request,"posts/index.html",
    {
        "posts":posts,
        "form":form
    })

def create(request):
    form = PostsCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request,"posts/create.html",{
        "form":form
    })
def destroy(request,id):
    post=Post.objects.get(id=id) 
    post.delete()  
    return redirect("index")
def edit(request,id):
    post=Post.objects.get(id=id) 
    form = PostsCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")

    return render(request,"posts/edit.html",{
        "form" : form,
        "post" : post
    })



def like(request,pk):
    post= get_object_or_404(Post, id=request.POST.get('post_id')) #whenever "post_id" is clicked #esm el button
    #post.likes.add(request.user)
    re

