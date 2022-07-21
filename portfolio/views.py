from django.shortcuts import render, get_object_or_404
from blog.models import Project2
from .models import Project


def main(requests):
    projects = Project.objects.all()
    return render(requests, 'portfolio/index.html', {'projects': projects})

#
# def blog(request):
#     projects = Project2.objects.order_by('-data')
#     return render(request, 'blog/all_blogs.html', {'projects': projects})


