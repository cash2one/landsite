from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models import Case, Category

class CaseListView(View):
    def get(self, request, *args, **kwargs):
        categorys = Category.objects.all()
        category = request.GET.get('category')
        try:
            category = Category.objects.get(pk=category)
            cases = Case.objects.filter(category=category)
        except:
            cases = Case.objects.all()
        paginator = Paginator(cases, 8)
        page = request.GET.get('page')
        try:
            case_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            case_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            case_list = paginator.page(paginator.num_pages)

        return render_to_response('case/case_list.html', {
                                                        "case_list": case_list,
                                                        "categorys": categorys,
                                                        })

class CaseDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        try:
            instance = Case.objects.get(pk=pk)
        except:
            instance = None
        print instance

        return render_to_response('case/case_detail.html', {"case": instance})