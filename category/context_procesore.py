from .models import Category

def menu_category_link(request):
      links = Category.objects.all()
      return dict(links=links)

