"""
Definition of models.
"""

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import re

class Tech(models.Model):
    name = models.CharField(max_length=200)
    img = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Mantra(models.Model):
    name = models.CharField(max_length=10)
    author = models.CharField(max_length=100)
    mantra = models.CharField(max_length=500)

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name

class Entry(models.Model):
    title = models.CharField(max_length=400, unique=True)
    name_fixed = models.CharField(max_length=500, unique=True, default='')
    body = RichTextUploadingField(max_length=10000)
    abstract = models.TextField(max_length=1000)
    date = models.DateTimeField()
    techs = models.ManyToManyField(Tech)
    isBlog = models.BooleanField(null=False, default=True)
    cover = models.CharField(max_length=300, blank=True, null=False, default='')
    cover_big = models.CharField(max_length=300, blank=True, null=False, default='')
    is_public = models.BooleanField(null=False, default=False)

    def get_name_fixed(self):
        textToReturn = re.sub(r'(\.)|(,)|(;)|(:)|(\()|(\))','',self.title).lower()
        return re.sub(r'(\s)','_',textToReturn)

    def __str__(self):
        toReturn = ""
        if self.isBlog: toReturn = "Blog(" + str(self.id) + "): "
        else: toReturn = "Project(" + str(self.id) + "): "
        toReturn = toReturn + self.title
        return toReturn

    def save(self, *args, **kwargs):
        self.name_fixed = self.get_name_fixed()
        super(Entry, self).save(*args, **kwargs)

