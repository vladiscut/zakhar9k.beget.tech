from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from bhome.views import *
from blagodarenie import settings
from django.views.static import serve as mediaserve
# from django.conf.urls import url

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('bhome.urls')),
    path('about/',include('about_fond.urls')),
    path('projects/',include('projects.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
else:
    urlpatterns += [re_path(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',mediaserve, {'document_root':settings.MEDIA_ROOT}),re_path(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$',mediaserve, {'document_root':settings.STATIC_ROOT}),]

