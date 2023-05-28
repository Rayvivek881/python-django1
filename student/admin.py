from django.contrib import admin
from student.models import Student

# Register your models here.
@admin.register(Student)
class ProductAdmin(admin.ModelAdmin):
  class Meta:
    model = Student