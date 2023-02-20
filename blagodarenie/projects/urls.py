from django.urls import path
from projects.views import *

urlpatterns = [
    path('', projects, name='projects'),
    path('project/<slug:proj_slug>/', show_project, name = 'project'),
    path('new/<slug:new_slug>/', show_new, name = 'new')
]