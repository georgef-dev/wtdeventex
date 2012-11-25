# -*- coding: utf-8

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('eventex',
    url(r'^$', 'core.views.homepage', name='homepage'),
    url(r'^inscricao/$', 'subscriptions.views.subscribe', name='subscribe'),
    url(r'^inscricao/(\d+)/$', 'subscriptions.views.success', name='success'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
