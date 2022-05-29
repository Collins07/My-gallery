from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404

# Create your views here.

def gallery(request):
    return render (request, 'photos/gallery.html')

def viewPhoto(request, pk):
    return render (request, 'photos/photo.html')


def addPhoto(request):
    return render (request, 'photos/add.html')        
