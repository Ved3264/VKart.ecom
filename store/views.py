from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q

def store(request,category_slug=None):
      categories=None
      products=None
      
      if category_slug!=None:
            categories = get_object_or_404(Category,slug=category_slug)
            product_store= Product.objects.all().filter(category=categories,is_available=True)
            paginator = Paginator(product_store,6)
            page = request.GET.get('page')
            paged_products = paginator.get_page(page)
            product_count = product_store.count()
      else:
           product_store  = Product.objects.all().filter(is_available=True).order_by('id')
           paginator = Paginator(product_store,6)
           page = request.GET.get('page')
           paged_products = paginator.get_page(page)
           product_count = product_store.count()
      context={
            'product_store':paged_products,
            'product_count':product_count,
      }
      return render(request,'stores/store.html',context)


def product_detail(request,category_slug,product_slug):
      try:
            single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
            in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request),product=single_product).exists()
      except Exception as e:
            raise e
      context={
            'single_product':single_product,
            'in_cart':in_cart,
      }
      return render(request,'stores/product_detail.html',context)

def search(request):
      if 'keyword' in request.GET:
            keyword = request.GET['keyword']
            if keyword:
                  product = Product.objects.order_by('-create_date').filter(Q(discription__icontains=keyword) | Q(product_name__icontains=keyword))
                  product_count = product.count()
                  context={
                  'product_store':product,
                  'product_count':product_count,
                   }
      return render(request,'stores/store.html',context)