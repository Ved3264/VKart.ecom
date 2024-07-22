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
      try:
            single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
      except Exception as e:
            raise e
      context={
            'single_product':single_product,
      }
      return render(request,'stores/product_detail.html',context)