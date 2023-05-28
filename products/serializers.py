from rest_framework import serializers

from .models import Product, testModel
from decimal import Decimal

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = [ 'id', 'title', 'content', 'price' ]

  def create(self, validated_data):
    return Product.objects.create(**validated_data)
    
  def update(self, instance, validated_data):
    for key, value in validated_data.items():
      if value is None:
        continue
      instance.__setattr__(key, value)
    instance.save()
    return instance

  
class testModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = testModel
    fields = [ 'Product', 'CreatedAt', 'UpdatedAt']
  
