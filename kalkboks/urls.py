from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'web.views.home', name='home'),
                       url(r'^api/', include('web.urls')),

                       # url(r'^blog/', include('blog.urls')),
                       url(r'^privacy/', TemplateView.as_view(template_name="privacy.html"),
                           name="privacy"),

                       url(r'^admin/', include(admin.site.urls)),
                       url('', include('django.contrib.auth.urls', namespace='auth')),
                       url(r'^accounts/', include('registration.backends.default.urls')),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
