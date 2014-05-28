from django.conf.urls import patterns, url

from main import views

#############################################
# Note that this file is currently not used #
#############################################

urlpatterns = patterns('',
                       url(r'^$', views.mainSite, name='mainSite'),
                       url(r'^about/$', views.about, name='aboutPage'),
                       url(r'^schedule/$', views.schedule, name='schedulePage'),
                       url(r'^membership/$', views.membership, name='membershipPage'),
                       url(r'^download/$', views.download, name='downloadPage'),
                       url(r'^contact/$', views.contact, name='contactPage'),
                       
#                       url(r'^$', views.mainSite, name='mainSite'),
#                       url(r'^$', views.mainSite, name='mainSite'),
)
