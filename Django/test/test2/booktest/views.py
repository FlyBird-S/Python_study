from django.shortcuts import render
from django.db.models import Max,F
from .models import *
# Create your views here.
def index(request):
    list = BookInfo.books1.filter(heroinfo__hcontent__contains="六")
    list=set(list)#去重
    list1 = BookInfo.books1.filter(bread__gt=F("bcommet"))  #使用 F对象可以进行字段与字段比较
    #list1 = BookInfo.books1.filter(Q(bread__gt=("bcommet"))|Q(pk__gt=4)) #利用Q对象可以进行逻辑或
    list1=set(list1)
    date = BookInfo.books1.aggregate(Max('bpub_date'))
    context={"list":list,
             'list1':list1,
             'date':date
             }
    return  render(request,'booktest/index.html',context)