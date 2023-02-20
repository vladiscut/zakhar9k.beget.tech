from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from .models import *
from projects.models import *

# @cache_page(60 * 2)
def index(request):
    project_main =  Projects.objects.filter(is_published = True).order_by('-time_update')
    partners = Partners.objects.filter(is_published=True)
    if project_main:
        project_main = project_main[0]
    return render(request,'bhome/index.html', {'project_main':project_main, 'partners':partners})

# @cache_page(60 * 2)
def about(request):
    return render(request,'bhome/about.html', {'title':'О фонде'})

def pageNotFound(request,exception):
    return  HttpResponseNotFound('NOT FOUND gofuckyourself')