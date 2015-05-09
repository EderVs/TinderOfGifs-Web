from django.conf.urls import patterns, url
from gif import api_views as gif_views

urlpatterns = patterns('',
	#Gifs
	url(r'^gifs/$', gif_views.AllGifsView.as_view(), name='get_all_gifs'),
)
