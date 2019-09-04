from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
from .forms import PostForm


def post_index(request):
    posts = Post.objects.all()
    return render(request,'post/index.html',{'posts':posts})

def post_detail(request,id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post':post,
    }
    return render(request,'post/detail.html', context)

def post_create(request):

    #if request.method == "POST":
    #    print(request.POST)

    #title = request.POST.get('title')
    #content = request.POST.get('content')
    #Post.objects.create(title = title, content = content)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'post/form.html', context)

def post_update(request):
    return HttpResponse('Burası post_update sayfası')

def post_delete(request):
    return HttpResponse('Burası post_delete sayfası')

