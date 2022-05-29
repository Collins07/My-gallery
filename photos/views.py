from unicodedata import category
from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
from .models import Category, Photo

# Create your views here.

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()


    context = {'categories':categories, 'photos':photos}
    return render (request, 'photos/gallery.html', context)



def viewPhoto(request):
    photo = Photo.objects.get()
    return render (request, 'photos/photo.html', {'photo':photo})





def addPhoto(request):
    return render (request, 'photos/add.html')        
