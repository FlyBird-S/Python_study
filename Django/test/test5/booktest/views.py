from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):

    return render(request,'booktest/index.html')

#中间间演示
def myexc(request):
    int("ww")
    return HttpResponse("ok")