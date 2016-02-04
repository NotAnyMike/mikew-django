"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from app.models import Person
from app.serializers import PersonSerializer

class JSONResponse(HttpResponse):
	def __init__(self, data, **kwargs):
		 content = JSONRenderer().render(data)
		 kwargs['content_type'] = 'application/json'
		 super(JSONResponse, self).__init__(content, **kwargs)

def person_detail(request, pk):
	try:
		person = Person.objects.get(pk=pk)
	except Person.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = PersonSerializer(person)
		return JSONResponse(serializer.data)
	else:
		return HttpResponse(status=404)

def person_list(request):
	if request.method == 'GET':
		persons = Person.objects.all()
		serializer = PersonSerializer(persons, many=True)
		return JSONResponse(serializer.data)
	else:
		return JSONResponse(serializer.errors, status=404)
