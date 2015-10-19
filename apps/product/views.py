from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models import Product, Category, Mine

class ProductListView(View):
    def get(self, request, *args, **kwargs):
        categorys = Category.objects.all()
        category = request.GET.get('category')
        try:
            category = Category.objects.get(pk=category)
            products = Product.objects.filter(category=category)
        except:
            products = Product.objects.all()
        paginator = Paginator(products, 8)
        page = request.GET.get('page')
        try:
            product_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            product_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            product_list = paginator.page(paginator.num_pages)

        return render_to_response('product/product_list.html', {
                                                        "product_list": product_list,
                                                        "categorys": categorys,
                                                        })

class ProductDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        try:
            instance = Product.objects.get(pk=pk)
        except:
            instance = None
        return render_to_response('product/product_detail.html', {"product": instance})

class MineDetail(View):
    def get(self, request, pk, *args, **kwargs):
        try:
            instance = Mine.objects.get(pk=pk)
        except:
            instance = None
        return render_to_response('product/mine_detail.html', {"mine": instance})