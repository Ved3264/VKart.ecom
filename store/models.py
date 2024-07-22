from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
      product_name   =  models.CharField(max_length=200,unique=True)
      slug           =  models.SlugField(max_length=200,unique=True)
      discription    =  models.CharField(max_length=500,blank=True)
      price          =  models.IntegerField()
      stock          =  models.IntegerField()
      image          =  models.ImageField(upload_to='photos/product')
      is_available   =  models.BooleanField(default=True)
      create_date    =  models.DateTimeField(auto_now_add=True)
      update_date    =  models.DateTimeField(auto_now=True)
      category       = models.ForeignKey(Category,on_delete=models.CASCADE)

      def get_url(self):
            return reverse('product_detail',args=[self.category.slug,self.slug])

      def __str__(self):
            return self.product_name
      