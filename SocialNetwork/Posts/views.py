from django.shortcuts import render,redirect
from .models import Post
from .forms import PostsCreateForm


# Create your views here.

def index(request):
    posts= Post.objects.all()
    print(posts)
    
    return render(request,"posts/index.html",
    {
        "posts":posts,
       

    })

def create(request):
    form = PostsCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request,"posts/create.html",{
        "form":form
    })