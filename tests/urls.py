import os

from django.conf.urls import include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^knowledge/', include('knowledge.urls')),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    #     {'document_root': os.path.join(
    #         os.path.dirname(__file__), '../knowledge/static'
    #     ).replace('\\', '/')})
]
