from django.shortcuts import render
from store.models import Product
from category.models import Category

# Create your views here.
def store(request,category_slug=None):
    if category_slug != None:
        categories=Category.objects.get(slug=category_slug)
        products=Product.objects.filter(category=categories,is_available=True)
    else:
        products=Product.objects.all().filter(is_available=True)
    products_count=products.count()

    context={
        'products':products,
        'products_count':products_count
    }
    return render(request,'store/store.html',context)

def product_details(request,category_slug,product_slug):
    try:
        single_product=Product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception as e:
        print(e)

    context={
        'single_product':single_product
    }
    return render(request,'store/product_detail.html',context)
