from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from filebrowser.sites import site

from apps.civilization.views import NewsDetailView

urlpatterns = [
    # Examples:
    # url(r'^$', 'landsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('apps.home.urls')),
    url(r'^product/', include('apps.product.urls')),
    url(r'^aboutus/', include('apps.aboutus.urls')),
    url(r'^civilization/', include('apps.civilization.urls')),
    url(r'^news/(?P<pk>\d+)/?', NewsDetailView.as_view(), name="news-detail"),
    url(r'^service/', include('apps.service.urls')),
    url(r'^case/', include('apps.case.urls')),
]