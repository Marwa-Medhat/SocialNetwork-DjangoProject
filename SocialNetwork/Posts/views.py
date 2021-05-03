from django.shortcuts import render,redirect
from .models import Post ,Comment

from .forms import PostsCreateForm ,CommentsCreateForm


# Create your views here.

def index(request):
    posts= Post.objects.order_by('-creation_date_time')
    print(posts)
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
    data = {'user_id': post.user_id_id, 'content': post.content} 
    form = PostsCreateForm(request.POST or None,initial=data)
    if form.is_valid():
        form.save()
        return redirect("index")

    return render(request,"posts/edit.html",{
        "form" : form,
        "post" : post
    })
def details(request,id):
    post=Post.objects.get(id=id)
    data = {'post_id': post.id}

    comment = CommentsCreateForm(request.POST or None,initial=data)
    
    form = PostsCreateForm(request.POST or None)
   
    if comment.is_valid():
        comment.post=post
        comment.save()
        return redirect("details",id=post.id)
    return render(request,"posts/details.html",{
        "form":form,
        "post":post,
        "comment":comment,
        
    })




