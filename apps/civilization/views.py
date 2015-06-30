from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models import News

class NewsListView(View):
    def get(self, request, *args, **kwargs):
        paginator = Paginator(News.objects.all(), 4)
        page = request.GET.get('page')
        try:
            news_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            news_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            news_list = paginator.page(paginator.num_pages)

        return render_to_response('civilization.html', {
                                                        "news_list": news_list,
                                                        })

class NewsDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        try:
            instance = News.objects.get(pk=pk)
        except:
            instance = None
        return render_to_response('news_detail.html', {"news": instance})