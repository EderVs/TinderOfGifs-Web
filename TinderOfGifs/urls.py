from django.conf.urls import patterns, include, url
from django.contrib import admin
from gif.views import AllGifsView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TinderOfGifs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^gifs/$', AllGifsView.as_view(), name='get_all_gifs'),
    url(r'^admin/', include(admin.site.urls)),
)
