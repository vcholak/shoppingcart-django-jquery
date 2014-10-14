from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import RedirectView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sports.views.home', name='home'),  # matches to '/' URL
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', 'django.contrib.staticfiles.views.serve', kwargs={
    #        'path': 'index.html', 'document_root': settings.STATIC_ROOT}),

    # http://127.0.0.1:8000/ causes: (404) Directory indexes are not allowed here.
    #url(r'^$', 'sports.views.home'),

    # redirect_to has been deprecated in Django 1.5, so use the class based RedirectView
    (r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico')),

    url(r'^admin/', include(admin.site.urls)),

    # "GET /api/product HTTP/1.1" 404 1623
    #url(r'^api/product$', 'sports.views.products'),
    #url(r'^api/', include('sports.urls')),

)

#urlpatterns += patterns(
#    url(r'^$', 'django.contrib.staticfiles.views.serve', kwargs={
#            'path': 'index.html', 'document_root': '/work/js/proAngularJS/app/'})  # STATICFILES_DIRS[0]})
#)

#if settings.DEBUG:
#    urlpatterns += patterns(
#        'django.views.static',
#        url(r'^$',
#        'serve',
#        {'path': 'index.html', 'document_root': settings.MEDIA_ROOT}), )

# UNDERNEATH your urlpatterns definition, add the following two lines:
#if settings.DEBUG:
#    urlpatterns += patterns(
#        'django.views.static',
#        (r'/(?P<path>.*)',
#        'serve',
#        {'document_root': settings.MEDIA_ROOT}), )

#if settings.DEBUG:
#    from django.views.static import serve
#    urlpatterns += patterns('',
#        url(r'^(?P<path>favicon\..*)$', serve, {'document_root': settings.STATICFILES_DIRS[0]}),
        #url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], serve, {'document_root': settings.MEDIA_ROOT}),
        #url(r'^%s(?P<path>.*)$' % settings.STATIC_URL[1:], 'django.contrib.staticfiles.views.serve', dict(insecure=True)),
#    )