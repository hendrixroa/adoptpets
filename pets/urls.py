from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns
from . import views

urlpatterns = [
        url(r'^$', views.main, name='main'),
]
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT}))
