from django.shortcuts import render
from .models import Product

def store(request):
      product_store  = Product.objects.all().filter(is_available=True)
      product_count = product_store.count()

      context={
            'product_store':product_store,
            'product_count':product_count,
      }
      return render(request,'stores/store.html',context)