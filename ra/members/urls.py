from django.conf.urls import patterns, url
from members import views

urlpatterns = patterns('',
                       url(r'^$', views.members, name='memberList'),
                       url(r'^add/$', views.addMember, name='addMember'),
                       url(r'^details/(?P<member_id>\d+)/$', views.memberDetails, name='itemDetails'),
)
