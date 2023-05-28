from django.db import models
from decimal import Decimal

# Create your models here.
class Product(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField(blank=True, null=True)
  price = models.DecimalField(max_digits=15 ,decimal_places=3, default=99.999)

  def __str__(self):
    return self.title  

class testModel(models.Model):
  CreatedAt = models.DateTimeField(auto_now_add=True)
  UpdatedAt = models.DateTimeField(auto_now=True)
  Product = models.ForeignKey(Product, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return self.Product.title
