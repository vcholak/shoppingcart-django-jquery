__author__ = 'vcholak'

from django.conf.urls import patterns, url, include
import sports.views as views

product_urls = patterns(
    url(r'^$', views.products)
)

urlpatterns = patterns(
    url(r'^product', include(product_urls)),
)