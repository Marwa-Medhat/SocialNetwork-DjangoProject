from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostsCreateForm


# Create your views here.


def index(request):
    posts = Post.objects.order_by('-creation_date_time')
    print(posts)
    form = PostsCreateForm()
    print(form)
    return render(request, "posts/index.html",
                  {
                      "posts": posts,
                      "form": form
                  })


def create(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('mustauth')
    form = PostsCreateForm(request.POST or None, user_id=request.user.username)
    if form.is_valid():
        form.save()
        return redirect("index")

    return render(request, "posts/create.html", {
        "form": form,
    })


def destroy(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect("index")


def edit(request, id):
    post = Post.objects.get(id=id)
    form = PostsCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")

    return render(request, "posts/edit.html", {
        "form": form,
        "post": post
    })


def details(request, id):
    post = Post.objects.get(id=id)
    form = PostsCreateForm()
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
    return render(request, "posts/details.html",
                  {
                      "post": post,
                      "form": form,
                      'is_liked': is_liked,
                      'total_likes': post.total_likes(),
                  })


def like_post(request):
    # whenever "post_id" is clicked #esm el button
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    # unlike post
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        # like post
        post.likes.add(request.user)
        is_liked = True
    return render(request, "posts/details.html",
                  {
                      "post": post,
                      'is_liked': is_liked,
                      'total_likes': post.total_likes()
                  })


def must_authenticate_view(request):
    return render(request, 'Posts/must_auth.html', {})
