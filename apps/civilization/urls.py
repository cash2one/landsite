from django.conf.urls import url
from views import NewsListView

urlpatterns = [
    url(r'^', NewsListView.as_view(), name="news-list"),
]