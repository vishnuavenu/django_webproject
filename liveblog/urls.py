from django.conf.urls import url, patterns
from liveblog.views import index, updateafter

urlpatterns = patterns('',
        url(r'^$', index ,name='update'),
        url(r'^updates-after/(?P<uid>\d+)/$', updateafter, name="updateafter"),
        )