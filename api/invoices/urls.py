from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
import views


urlpatterns = [
    url(r'^invoices/$', views.InvoiceList.as_view()),
    url(r'^invoices/(?P<pk>[0-9]+)/$', views.InvoiceDetail.as_view()),
]
