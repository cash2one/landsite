from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Examples:
    # url(r'^$', 'landsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('apps.home.urls')),
    url(r'^product/', include('apps.product.urls')),
    url(r'^aboutus/', include('apps.aboutus.urls')),
    url(r'^civilization/', include('apps.civilization.urls')),
    url(r'^service/', include('apps.service.urls')),
    url(r'^case/', include('apps.case.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()