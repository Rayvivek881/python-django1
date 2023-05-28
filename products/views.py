from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from pathlib import Path
from products.models import Product, testModel
from django.forms.models import model_to_dict
from rest_framework.parsers import JSONParser
import json
import io

from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from products.serializers import ProductSerializer


@api_view(['POST', 'GET'])
def homePage(request, *args, **kwargs) -> JsonResponse:
  if request.method == "POST":
    print(json.loads(request.body))
    return JsonResponse({
      "message" : "POST homePage"
    })
  
  if request.method == "GET":
    return JsonResponse({
      "message" : "GET homePage"
    })

@api_view(['GET'])
def getAllProducts(request, *args, **kwargs) -> JsonResponse:
  products = Product.objects.all()
  return JsonResponse({
    "products" : list(products.values()),
    "message" : f"{Path(__file__).absolute()} getAllProducts",
  })

@api_view(['GET'])
def getRandomProduct(request, *args, **kwargs) -> JsonResponse:
  product = Product.objects.order_by("?").first()
  return JsonResponse({
    "product" : model_to_dict(product),
    "bySerializer" : ProductSerializer(product).data,
    "message" : f"{Path(__file__).absolute()} getRandomProduct",
  })

@csrf_exempt
@api_view(['POST'])
def createProduct(request, *args, **kwargs) -> JsonResponse:
  data = json.loads(request.body)
  product = Product.objects.create(**data)
  return JsonResponse({
    "product" : model_to_dict(product),
    "message" : f"{Path(__file__).absolute()} createProduct",
  })

@api_view(['PUT', 'DELETE'])
def updateAndDelete(request, id,  *args, **kwargs) -> JsonResponse:
  if request.method == 'PUT' and id is not None:
    stream = io.BytesIO(request.body)
    data = JSONParser().parse(stream)
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(instance=product, data=data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse({
        "product" : serializer.data,
        "message" : f"{Path(__file__).absolute()} updateProduct",
      })
    else:
      return getErrorObject(serializer.errors)
    
  if request.method == 'DELETE' and id is not None:
    product = Product.objects.get(id=id)
    product.delete()
    return JsonResponse({
      "product" : {},
      "message" : f"product {id} deleted",
    })
  
  return getErrorObject("id is required")

@api_view(['GET'])
def getAllTestModels(request, *args, **kwargs) -> JsonResponse:
  testModels = testModel.objects.all()
  return JsonResponse({
    "testModels" : list(testModels.values()),
    "message" : f"{Path(__file__).absolute()} getAllTestModels",
  })

@api_view(['GET'])
def getTastModelByProductID(request, id, *args, **kwargs) -> JsonResponse:
  testModels = testModel.objects.filter(Product=id)
  return JsonResponse({
    "testModels" : list(testModels.values()),
    "message" : f"{Path(__file__).absolute()} getTastModelByProductID",
  })

@api_view(['POST'])
def createTestModel(request, *args, **kwargs) -> JsonResponse:
  data = json.loads(request.body)
  testModel = testModel.objects.create(**data)
  return JsonResponse({
    "testModel" : model_to_dict(testModel),
    "message" : f"{Path(__file__).absolute()} createTestModel",
  })


def getErrorObject(message) -> JsonResponse:
  return JsonResponse({
    "location" : f"{Path(__file__).absolute()} error",
    "message" : message,
  })