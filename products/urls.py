from django.urls import path
from products.views import *

urlpatterns = [
  path("", homePage),
  path("allproducts/", getAllProducts),
  path("createproducts/", createProduct),
  path("products/<int:id>", updateAndDelete),
  path("randomproduct/", getRandomProduct),
  path("alltestmodels/", getAllTestModels),
  path("testmodelbyproductid/<int:id>/", getTastModelByProductID),
  path("createtestmodel/", createTestModel),
]
