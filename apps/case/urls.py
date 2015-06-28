from django.conf.urls import url
from views import CaseListView, CaseDetailView

urlpatterns = [
    url(r'^list/?', CaseListView.as_view(), name="case-list"),
    url(r'^detail/(?P<pk>\d+)/?', CaseDetailView.as_view(), name="case-detail"),
]