from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	# /card/named/**help file**
	url(r'^named/$', views.detail_help, name='detail_help'),
	# /card/named/sandstorm_titan
	url(r'^named/(?P<card_name>[\w\-]+)/$', views.detail, name='detail'),
	# /chatter
	url(r'^chatter/$', views.chatter, name='chatter'),
	# /chatter/392
	url(r'^chatter/(?P<chatter_id>[0-9]+)/$', views.chatter_detail, name='chatter_detail')
]
