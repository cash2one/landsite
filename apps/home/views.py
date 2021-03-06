from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from apps.product.models import IndexProduct, Mine

class IndexPage(View):
    def get(self, request, *args, **kwargs):
        product_list = IndexProduct.objects.all()
        mine_list = Mine.objects.all()
        return render_to_response('index.html', {
                                                        "product_list": product_list,
                                                        "mine_list": mine_list,
                                                        })