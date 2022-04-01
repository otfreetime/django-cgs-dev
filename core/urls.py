# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls")),
    path('devapp/', include('apps.devapp.urls')), 
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    #path('devapp/', include("apps.devapp.urls")), 
    #path('tag/', include("apps.mytags.urls"))  
]


# urlpatterns = [
#     path('author-polls/', include('polls.urls', namespace='author-polls')),
#     path('publisher-polls/', include('polls.urls', namespace='publisher-polls')),
# ]