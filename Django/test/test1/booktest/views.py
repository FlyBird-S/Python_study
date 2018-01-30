from django.shortcuts import render
from . import models
from django.http import *
from django.template import  RequestContext,loader
# Create your views here.
def index(request):
    book_list = models.Book_Info.objects.all()
    context={'list':book_list}
    return render(request,'booktest/index.html',context) #加载temp并解析
def show(request,get_re_id):
    book = models.Book_Info.objects.get(pk=get_re_id)
    herolist = book.hero_info_set.all()
    context={"list":herolist}
    return render(request,'booktest/show.html',context) #加载temp并解析