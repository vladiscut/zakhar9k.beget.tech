from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from about_fond.models import DocumentsFond
from django.views.decorators.cache import cache_page
from bhome.models import Partners


# @cache_page(60 * 2)
def about(request):
    docs = DocumentsFond.objects.filter(is_fond=True)
    partners = Partners.objects.filter(is_published=True)
    context = {'title':'О фонде',
               'partners':partners,
               'docs': docs}
    return render(request,'about_fond/about.html', context)

def pageNotFound(request,exception):
    return  HttpResponseNotFound('NOT FOUND gofuckyourself')