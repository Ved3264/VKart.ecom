from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import Category

def store(request,category_slug=None):
      categories=None
      products=None
      
      if category_slug!=None:
            categories = get_object_or_404(Category,slug=category_slug)
            product_store= Product.objects.all().filter(category=categories,is_available=True)
            product_count = product_store.count()
      else:
           product_store  = Product.objects.all().filter(is_available=True)
           product_count = product_store.count()
      context={
            'product_store':product_store,
            'product_count':product_count,
      }
      return render(request,'stores/store.html',context)


def product_detail(request,category_slug,product_slug):
      return render(request,'stores/product_detail.html')