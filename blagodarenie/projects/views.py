from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page

from projects.models import *

# @cache_page(60 * 15)
def projects(request):
    projects = Projects.objects.all()
    return render(request,'projects/projects.html', {'title':'Проекты','projects':projects})

def show_project(request, proj_slug):
    project = get_object_or_404(Projects,slug=proj_slug)
    news = News.objects.filter(project_id=project.pk, is_published= True)
    docs = Documents.objects.filter(project_id=project.pk)

    context = {'title':project.title,
               'project':project,
               'news':news,
               'docs':docs}

    return render(request,'projects/about_project.html', context)

def show_new(request, new_slug):
    new = get_object_or_404(News,slug=new_slug)

    context = {'new':new,}

    return render(request,'projects/new_post.html', context)

def pageNotFound(request,exception):
    return  HttpResponseNotFound('NOT FOUND')
