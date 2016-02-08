"""
Definition of models.
"""

from django.db import models
from tinymce.models import HTMLField

class Tech(models.Model):
	name = models.CharField(max_length=200)
	img = models.CharField(max_length=200)

class Mantra(models.Model):
	name = models.CharField(max_length=10)
	author = models.CharField(max_length=100)
	mantra = models.CharField(max_length=500)

class Person(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	mobile = models.CharField(max_length=20)
	facebook_username = models.CharField(max_length=50)
	twitter_username = models.CharField(max_length=50)
	medium_username = models.CharField(max_length=50)
	github_username = models.CharField(max_length=50)
	img = models.CharField(max_length=100)
	img2x = models.CharField(max_length=100)
	interests = models.CharField(max_length=500)
	mantra = models.ForeignKey(Mantra, blank=True, null=True, on_delete=models.SET_NULL)
	techs = models.ManyToManyField(Tech)

class Entry(models.Model):
    title = models.CharField(max_length=400)
    name_fixed = models.CharField(max_length=500)
    body = HTMLField(max_length=10000)
    date = models.DateTimeField()
    techs = models.ManyToManyField(Tech)
    isBlog = models.BooleanField(null=False, default=True)
    cover = models.CharField(max_length=300, blank=True, null=False, default='')
    cover_big = models.CharField(max_length=300, blank=True, null=False, default='')
