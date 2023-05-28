from django.contrib import admin
from django.urls import path, include
from .views import StudentAPI

urlpatterns = [
  path('', StudentAPI.as_view(), name='student' ),
]