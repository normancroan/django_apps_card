from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	# ex: /card/4
	url(r'^(?P<card_id>[0-9]+)/$', views.detail, name='detail'),
	# /chatter
	url(r'^chatter/$', views.index, name='chatter')
]
