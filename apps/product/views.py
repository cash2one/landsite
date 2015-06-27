from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models import Product

class ProductListView(View):
    # model = Product
    # paginator = Paginator(model.objects.all(), 8) 

    def get(self, request, *args, **kwargs):
        paginator = Paginator(Product.objects.all(), 8)
        print paginator.count
        page = request.GET.get('page')
        print page
        try:
            product_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            product_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            product_list = paginator.page(paginator.num_pages)

        print product_list

        return render_to_response('product/product_list.html', {"product_list": product_list})





class ProductDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        try:
            instance = Product.objects.get(pk=pk)
        except:
            instance = None
        print instance

        return render_to_response('product/product_detail.html', {"product": instance})