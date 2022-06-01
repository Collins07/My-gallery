from unicodedata import name
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.gallery, name='gallery',),
    url(r'^photo/<slug:slug>',views.viewPhoto, name='photo',),
    url(r'^add/', views.addPhoto, name='add',),
]
