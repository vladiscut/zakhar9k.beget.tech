from django.urls import path
from about_fond.views import *

urlpatterns = [
    path('', about, name='about')
]