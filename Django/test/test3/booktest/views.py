from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse(request.path + "!!!")


def detail(request, num):
    return HttpResponse(str(num))


# GET测试显示页面 以/?a=xx& 方式传值
def getTest1(request):
    return render(request, 'booktest/getTest1.html')


# 接收一键一值
def getTest2(request):
    #根据键接收值
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {'a': a1, 'b': b1, 'c': c1}
    return render(request, 'booktest/getTest2.html', context)


def getTest3(request):
    return render(request, 'booktest/getTest3.html')
