from django.contrib import admin
from products.models import Product, testModel

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'content', 'price']
  class Meta:
    model = Product
    

@admin.register(testModel)
class testModelAdmin(admin.ModelAdmin):
  list_display = ['Product', 'UpdatedAt', 'CreatedAt']
  class Meta:
    model = testModel