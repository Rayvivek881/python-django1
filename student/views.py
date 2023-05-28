from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
  def get(self, request, *args, **kwargs):
    return JsonResponse({
      'name': 'John', 'age': 20
    })
  
  def post(self, request, *args, **kwargs):
    return HttpResponse('POST request')

  def put(self, request, id,  *args, **kwargs):
    return HttpResponse('PUT request')

  def delete(self, request, id, *args, **kwargs):
    return HttpResponse('DELETE request')
  
  def patch(self, request, id, *args, **kwargs):
    return HttpResponse('PATCH request')