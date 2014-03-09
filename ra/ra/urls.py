from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from main import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ra.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
                       

                       url(r'^$', views.mainSite, name='mainSite'),
                       url(r'^about/$', views.about, name='aboutPage'),
                       url(r'^schedule/$', views.schedule, name='schedulePage'),
                       url(r'^membership/$', views.membership, name='membershipPage'),
                       url(r'^contact/$', views.contact, name='contactPage'),
                       #url(r'^$', include('main.urls')),
                       url(r'^inventory/', include('inventory.urls')),
                       url(r'^admin/', include(admin.site.urls)),
)

