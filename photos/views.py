from django.shortcuts import render,redirect
from .models import Category,Photo

# Create your views here.

def gallery(request):
    category=request.GET.get('category')
    if category==None:
        photos=Photo.objects.all()
    else:
        photos=Photo.objects.filter(category__name=category)


    categories=Category.objects.all()
    context={'categories':categories,'photos':photos}
    return render(request,'gallery.html',context)

def add(request):
    categories=Category.objects.all()

    if request.method=='POST':
        data=request.POST
        image=request.FILES.get('image')

        if data['category'] != 'none':
            category=Category.objects.get(id=data['category'])
        elif data['newCategory'] !='':
            category, created=Category.objects.get_or_create(name=data['newCategory'])
        else:
            category=None

        photo=Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )
        return redirect('gallery')

    context={'categories':categories}
    return render(request,'add.html',context)

def photo(request,pk):
    photo=Photo.objects.get(id=pk)
    # Add your logic here
    return render(request, 'photo.html',{'photo':photo})
