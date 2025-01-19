from django.shortcuts import render, get_object_or_404
from blog.models import Post
# Create your views here.


def blog_view(request):
    posts= Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    posts= Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)  # This will raise 404 if post doesn't exist or is not published.
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)

def test(request, pid):
    # posts= Post.objects.get(id=pid)
    post = get_object_or_404(Post, pk=pid)  # This will raise 404 if post doesn't exist or is not published.
    context = {'post': post}
    return render(request, 'test.html', context)