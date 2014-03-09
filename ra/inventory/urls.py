from django.conf.urls import patterns, url
from inventory import views

urlpatterns = patterns('',
                       
                       url(r'^$', views.inventory, name='inventoryList'),
                       url(r'^item/(?P<item_id>\d+)/$', views.item_details, name='itemDetails'),
)
