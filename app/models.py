"""
Definition of models.
"""

from django.db import models

class Tech(models.Model):
	name = models.CharField(max_length=200)
	img = models.CharField(max_length=200)

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
	techs = models.ManyToManyField(Tech)

class Mantra(models.Model):
	name = models.CharField(max_length=10)
	author = models.CharField(max_length=100)
	mantra = models.CharField(max_length=500)
