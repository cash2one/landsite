from django.conf.urls import url
from views import ProductListView, ProductDetailView

urlpatterns = [
    url(r'^list/?', ProductListView.as_view(), name="product-list"),
    url(r'^detail/(?P<pk>\d+)/?', ProductDetailView.as_view(), name="product-detail"),
]