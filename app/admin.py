from django.contrib import admin

from .models import Person, Tech, Mantra

admin.site.register(Person)
admin.site.register(Tech)
admin.site.register(Mantra)
