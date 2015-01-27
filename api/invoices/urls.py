from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
import views


urlpatterns = [
    url(r'^invoice/$', views.InvoiceList.as_view()),
    url(r'^invoice/(?P<pk>[0-9]+)/$', views.InvoiceList.as_view()),
]
