"""
Book: Building RESTful Python Web Services
"""
from django.urls import re_path
from dogs import views

urlpatterns = [
    #re_path(r'^dogs/$', views.DogList.as_view(), name=views.DogList.name),
    #re_path(r'^dogs/(?P<pk>[0-9]+)/$', views.DogList.as_view()),
    re_path(r'^breeds/$', views.BreedList.as_view()),
    re_path(r'^breeds/(?P<pk>[0-9]+)/$', views.BreedDetail.as_view()),
    re_path(r'^dogs/$', views.DogList.as_view()),
    re_path(r'^dogs/(?P<pk>[0-9]+)/$', views.DogDetail.as_view()),
]
