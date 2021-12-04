from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostForm

def home(request):
    posts=Post.objects.all()
    return render(request,'home.html',{"posts":posts,"section":"home"})

def about(request):
    return render(request,'about.html')

def details(request,slug=None):
    post=get_object_or_404(Post,slug=slug)
    return render(request,'detail.html',context={"post":post,"section":"details"})

def create(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.auther = request.user
            post.save()
    else:
        form=PostForm()
    return render(request,"create.html",context={
        "section":"blog_create",
        "form":form
    })


def edit(request, pk=None):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
        return render(request, 'edit.html',
        {'section': 'blog_edit',
        'form': form,
        'post': post,
        })