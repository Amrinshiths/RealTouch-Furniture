from django.shortcuts import render
from .models import *
from product.models import *

# Create your views here.
def ProductCategoryList(request, id,):
    category = Category.objects.get(id=id)
    products = Product.objects.filter(category=category)
    context ={
        'category': category, 
        'product': products
            }
    print(category)

    return render(request, 'User-Template\Category\category_detail.html', context)
