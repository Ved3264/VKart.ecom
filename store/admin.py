from django.contrib import admin

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
      prepopulated_fields={'slug':('product_name',)}
      list_display = ('product_name','category','price','stock','create_date','update_date','is_available')
      readonly_fields =('create_date',)


admin.site.register(Product,ProductAdmin)
