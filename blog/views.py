from django.shortcuts import render, get_object_or_404
from .models import Project2


def blogs(requests):
    projects = Project2.objects.order_by('-data')
    return render(requests, 'blog/all_blogs.html', {'projects': projects})


def detail(request, blog_id):
    blog = get_object_or_404(Project2, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
