from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
                       url(r'^$', views.mainSite, name='mainSite'),
                       url(r'^about/$', views.about, name='aboutPage'),
                       url(r'^schedule/$', views.schedule, name='schedulePage'),
                       url(r'^membership$', views.membership, name='membershipPage'),
                       url(r'^contact$', views.contact, name='contactPage'),
#                       url(r'^$', views.mainSite, name='mainSite'),
#                       url(r'^$', views.mainSite, name='mainSite'),
)
