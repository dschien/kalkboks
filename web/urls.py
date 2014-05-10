__author__ = 'schien'
from django.conf.urls import patterns, url

# Routers provide an easy way of automatically determining the URL conf

from web import views


urlpatterns = patterns('',
                       url(r'^cagr', views.cagr),
)
