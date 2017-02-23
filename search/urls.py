from django.conf.urls import url
from . import views

app_name = 'search'
urlpatterns = [
	#url(),
	url(r'^$', views.index, name='index'),
	url(r'^result/(?P<group>\d+)/(?P<day>\d+)/$', views.result),
	url(r'^result/(?P<group>\d+)/(?P<day>\d+)/(?P<week_type>\d+)/$', views.result),	
]