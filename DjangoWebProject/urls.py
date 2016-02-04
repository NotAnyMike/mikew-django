"""
Definition of urls for DjangoWebProject.
"""

from datetime import datetime
from django.conf.urls import include, patterns, url
from app.forms import BootstrapAuthenticationForm
from DjangoWebProject.settings import STATIC_ROOT
from django.views.generic.base import RedirectView

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^api/', include('app.urls')),
	url(r'^admin/', admin.site.urls),
	url(r'^$', RedirectView.as_view(url='/index.html')),
	url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT, 'show_indexes' : True}),
	url(r'^(.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT, 'show_indexes' : True}),
)
