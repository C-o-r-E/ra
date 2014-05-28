from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from main import views

urlpatterns = patterns('',
                       url(r'^$', views.mainSite, name='mainSite'),
                       url(r'^about/$', views.about, name='aboutPage'),
                       url(r'^schedule/$', views.schedule, name='schedulePage'),
                       url(r'^membership/$', views.membership, name='membershipPage'),
                       url(r'^contact/$', views.contact, name='contactPage'),
                       url(r'^inventory/', include('inventory.urls')),
                       url(r'^download/$', views.download, name='downloadPage'),
                       url(r'^boss/', include(admin.site.urls)),
                       url(r'^ohaigithub/$', views.gitHook, name='gitHook'),
                       url(r'^login/$', views.user_login, name="userLogin"),
                       url(r'^logout/$', views.user_logout, name="userLogout"),
                       url(r'^absolut/$', views.absolut, name="absolutPage"),

)

