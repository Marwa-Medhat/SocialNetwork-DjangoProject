from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from Groups.models import Group
from .forms import PostsCreateForm, CommentsCreateForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from Notifications.models import Notification
# Create your views here.


def index(request):

    posts = Post.objects.filter(Group_id__isnull=True)
    posts = posts.order_by('-creation_date_time')
    print(posts)
    form = PostsCreateForm()
    # print(form)
    return render(request, "posts/index.html",
                  {
                      "posts": posts,
                      "form": form,

                  })


def create(request):
    # user = request.user
    # if not user.is_authenticated:
    #     return redirect('mustauth')
    global post
    form = PostsCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user_id = request.user
        content = form.cleaned_data.get('content')
        if form.cleaned_data.get('post_image'):
            postImg = form.cleaned_data.get('post_image')
            post = Post(content=content, post_image=postImg, user_id=user_id)
        else:
            post = Post(content=content, user_id=user_id)
        url = request.META.get('HTTP_REFERER')
        url = url.split("/")
        if len(url) == 5:
            if url[3] == "groups":
                groupId = url[4]
                group = Group.objects.get(pk=groupId)
                post.Group_id = group
        post.save()
        #forms = form.save(commit=False)
        #forms.user_id_id = request.user.id
        # forms.save()
        # return redirect("index")
        # return HttpResponseRedirect(request.path_info)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, "posts/create.html", {
        "form": form,
    })


def destroy(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect("index")


def edit(request, id):
    post = Post.objects.get(id=id)
    form = PostsCreateForm(request.POST or None,
                           request.FILES or None, instance=post)
    if form.is_valid():
        forms = form.save(commit=False)
        forms.user_id_id = request.user.id
        form.save()
        return redirect("index")

    return render(request, "posts/edit.html", {
        "form": form,
        "post": post
    })


def details(request, id):
    post = Post.objects.get(id=id)
    data = {'post_id': post.id}
    comment = CommentsCreateForm(request.POST or None, initial=data)
    form = PostsCreateForm(request.POST or None)
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    return render(request, "posts/details.html", {
        "form": form,
        "post": post,
        "comment": comment,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),

    })


def comment(request, id):
    post = Post.objects.get(id=id)
    data = {'post_id': post.id}
    comment = CommentsCreateForm(request.POST or None, initial=data)
    if comment.is_valid():
        comments = comment.save(commit=False)
        comments.user_id = request.user.id
        comments.save()
        if(request.user.username!=post.user_id.username):       

            content = f'{request.user.first_name} {request.user.last_name} commented in your post'
            Notification.objects.create(senderUser=request.user,RecieverUser=post.user_id,content=content ,  post=post)

        return redirect("details", id=post.id)
    return HttpResponseRedirect(post.get_absolute_url())
  
def like_post(request):
    # whenever "post_id" is clicked #esm el button
    post = get_object_or_404(Post, id=request.POST.get('post_id'))

    # unlike post
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
        notifiction = Notification.objects.get(senderUser=request.user,RecieverUser=post.user_id,content=f'{request.user.first_name} {request.user.last_name} liked your post',  post=post ).delete()
       
    else:
        # like post
        post.likes.add(request.user)
        is_liked = True
        if(request.user.username!=post.user_id.username):       
            content = f'{request.user.first_name} {request.user.last_name} liked your post'
            Notification.objects.create(senderUser=request.user,RecieverUser=post.user_id,content=content,  post=post )
    # return render(request,"posts/details.html",
    # {
    #     "post":post,
    #     'is_liked':is_liked,
    #     #     'total_likes': post.total_likes()
    # })

    return HttpResponseRedirect(post.get_absolute_url())


def must_authenticate_view(request):
    return render(request, 'Posts/must_auth.html', {})
