from django.shortcuts import render
from .models import *
from .forms import *
from morefeature.models import *
from product.models import *
from django.db.models import Q  # New


# Create your views here.

def Base(request):
    
    return render(request,'User-Template/base-layout.html')


def homepage(request):
    slider = Slider.objects.all().order_by('-id')[:4]
    hero = Hero.objects.all().order_by('-id')[0:1]
    brand = ClientBrand.objects.all().order_by('-id')
    context={
        'slider' :slider,
        'hero':hero,
        'brand' : brand,
    }
    return render(request,'User-Template/Landing-page/home_page.html',context)

def Search(request):
    print(request.POST)
    query = request.POST['query']
    product =Product.objects.filter(status=True,title__icontains=query)
    context = {
        'product':product
    }
    return render(request,'User-Template/Landing-page/search.html',context)