from django.conf.urls import patterns, include, url
from django.contrib import admin

from django_webproject import settings
import photogallery


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_webproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^webphotogallery/$', include('photogallery.urls')),
    
)

if settings.DEBUG:
    urlpatterns += patterns(
                            'django.views.static',
                            (r'^media/(?P<path>.*)',
                            'serve',
                            {'document_root': settings.MEDIA_ROOT }),
                            )
    
