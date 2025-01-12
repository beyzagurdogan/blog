from django.shortcuts import render
from .models import Blog

def blog_home(request):
    posts = Blog.objects.all()  # Tüm blog yazılarını al
    return render(request, 'blog/home.html', {'posts': posts})
