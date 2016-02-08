from django.conf.urls import url
from app import views

urlpatterns = [
	url(r'^persons/$', views.person_list),
	url(r'^persons/(?P<pk>[0-9]+)/$', views.person_detail),
	url(r'^blogs/$', views.blog_list),
	url(r'^blogs/(?P<pk>[0-9]+)/$', views.blog_detail),
]
