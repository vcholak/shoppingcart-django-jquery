from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import RedirectView

urlpatterns = patterns('',

    url(r'^$', 'sports.views.home', name='home'),  # matches to '/' URL

    # redirect_to has been deprecated in Django 1.5, so use the class based RedirectView
    (r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^order$', 'sports.views.order', name='order'),
)