from enum import unique
from unicodedata import category
from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
from .models import Category, Photo

# Create your views here.

def gallery(request):
    category = request.GET.get('category')
    
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)    

    categories = Category.objects.all()


    context = {'categories':categories, 'photos':photos}
    return render (request, 'photos/gallery.html', context)



def viewPhoto(request, slug):

    photo = Photo.objects.filter(slug=slug)
    return render (request, 'photos/photo.html', {'photo':photo})





def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=['category_new'])
        else:
            category = None

        photo = Photo.objects.create(
            category = category,
            description = data['description'],
            image = image,
            date_created= data['date_created'],
        )    

        return redirect ('gallery')   
        


    context = {'categories':categories}

    return render (request, 'photos/add.html', context)        
