from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.


def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blogs/allblogs.html', {'blogs': blogs})


def detail(request, blogs_id):
    blog_detail = get_object_or_404(Blog, pk=blogs_id)
    return render(request, 'blogs/detail.html', {'blog': blog_detail})
