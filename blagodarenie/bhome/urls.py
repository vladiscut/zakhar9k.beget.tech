from django.urls import path
from bhome.views import *

urlpatterns = [
    path('',index, name = 'home'),
]