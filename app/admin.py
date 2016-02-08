from django.contrib import admin

from .models import Person, Entry, Tech, Mantra

admin.site.register(Person)
admin.site.register(Tech)
admin.site.register(Mantra)
admin.site.register(Entry)
