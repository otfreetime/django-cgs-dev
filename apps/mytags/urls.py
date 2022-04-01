
from django.urls import  path, re_path as url
from django.views.generic.base import View
from .views import  index

urlpatterns = [
       path('', index, name="index"),

]
