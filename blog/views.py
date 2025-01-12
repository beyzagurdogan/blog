from django.shortcuts import render, get_object_or_404
from .models import Blog


def blog_home(request):
    posts = Blog.objects.all()  # Tüm blog yazılarını al
    return render(request, 'blog/home.html', {'posts': posts})



def blog_detail(request, blog_id):
    post = get_object_or_404(Blog, id=blog_id)  # Yazıyı al veya 404 döndür
    return render(request, 'blog/detail.html', {'post': post})
