"""
Definition of views.
"""

from django.http import HttpRequest, HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from app.models import Person, Entry
from app.serializers import PersonSerializer, EntrySerializer

@api_view(['GET'])
def person_detail(request, pk, format=None):
	try:
		person = Person.objects.get(pk=pk)
	except Person.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = PersonSerializer(person)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def person_list(request, format=None):
	if request.method == 'GET':
		persons = Person.objects.all()
		serializer = PersonSerializer(persons, many=True)
		return Response(serializer.data)
	else:
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def blog_list(request, format=None):
    if request.method == 'GET':
            blogs = Entry.objects.filter(isBlog=True)
            serializer = EntrySerializer(blogs, many=True)
            return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def blog_detail(request, pk, format=None):
    try:
        entry = Entry.objects.get(pk=pk, isBlog=True)
    except Entry.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogSerializer(entry)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
