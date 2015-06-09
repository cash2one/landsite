from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^', TemplateView.as_view(template_name="index.html")),
]