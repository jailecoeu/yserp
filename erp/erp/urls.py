from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^$', 'erp.views.home', name='home'),
    url(r'^account/',include('account.urls')),
    url(r'^system/',include('system.urls')),
    url(r'^car/',include('carsales.urls')),
)
