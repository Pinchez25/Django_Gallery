from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Category, Photo


# Create your views here.

def gallery(request):
    category = request.GET.get('category')
    
    if category is None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name__iexact=category)
    categories = Category.objects.all()

    return render(request, 'gallery/index.html', {
        'categories': categories,
        'photos': photos,
    })


def viewPhoto(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'gallery/photo.html', {
        'photo': photo,
    })


def addPhoto(request):
    categories = Category.objects.all()

    if request.method == "POST":
        data = request.POST
        image = request.FILES.get('image')

        if data.get('category') != 'none':
            category = Category.objects.get(id=data['category'])
        elif data.get('category_new') != "":
            category, created = Category.objects.get_or_create(name=data.get('category_new'))
        else:
            category = None

        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image
        )
        photo.save()
        return redirect(reverse('gallery'))

    return render(request, 'gallery/add.html', {
        'categories': categories,
    })
