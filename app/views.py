"""
Definition of views.
"""

from django.http import HttpRequest, HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from app.models import Person, Entry
from app.serializers import PersonSerializer, BlogSerializer, ProjectSerializer, BlogSummarySerializer, ProjectSummarySerializer

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
        blogs = Entry.objects.filter(isBlog=True, is_public=True)
        serializer = BlogSummarySerializer(blogs, many=True)
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

@api_view(['GET'])
def project_list(request, format=None):
    if(request.method == 'GET'):
        projects = Entry.objects.filter(isBlog=False, is_public=True)
        serializer = ProjectSummarySerializer(projects, many=True)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def project_detail(request, pk, format='json'):
    try:
        project =Entry.objects.get(pk=pk, isBlog=False)
    except Entry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def project_detail_by_name(request, pk, format='json'):
    try:
        project = Entry.objects.get(name_fixed=pk, isBlog=False)
    except Entry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def blog_detail_by_name(request, pk, format='json'):
    try:
        blog = Entry.objects.get(name_fixed=pk, isBlog=True)
    except Entry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
