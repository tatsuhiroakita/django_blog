from django.shortcuts import render
from .models import Blog


def index(request):
    blogs = Blog.objects.order_by('-created_datetime')
    return render(request, 'blogs/index.html', {'blogs': blogs})


def detail(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, 'blogs/detail.html', {'blog': blog})
