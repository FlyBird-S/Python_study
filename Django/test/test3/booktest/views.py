from django.shortcuts import render,redirect
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
    # 根据键接收值
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {'a': a1, 'b': b1, 'c': c1}
    return render(request, 'booktest/getTest2.html', context)


def getTest3(request):
    a_list = request.GET.getlist('a')
    context = {'a_list': a_list}
    return render(request, 'booktest/getTest3.html', context)


# from 标签中 name 属性会作为键 value会作为值
def postTest1(request):
    return render(request, 'booktest/postTest1.html')


def postTest2(request):
    uname = request.POST['uname']  # == uname=request.POST.get('uname')
    upwd = request.POST['upwd']
    ugender = request.POST['ugender']
    uhobby = request.POST.getlist('uhobby')
    context = {'uname': uname, "upwd": upwd, 'ugender': ugender, 'uhobby': uhobby}
    return render(request, 'booktest/postTest2.html', context)


def cookieTest(request):
    response = HttpResponse()
    cookie = request.COOKIES
    if "t1" in cookie:
        response.content=cookie['t1']
    response.set_cookie('t2', 'def')
    return response
# 重定向
def redTest1(request):
    #return HttpResponseRedirect('/booktest/redTest2/')
    return  redirect('/booktest/redTest2/') # 与上句效果相等
def redTest2(request):
    return HttpResponse('重定向网页')

#session 连续   注意 session需要连接数据库
def session1(request):
    uname = request.session.get('my_name',default="未登录")
    context = {"uname":uname}
    return render(request,'booktest/session1.html',context)
def session2(request):
    return render(request,'booktest/session2.html')
def session2_handle(request):
    uname = request.POST.get('uname')
    request.session['my_name'] = uname
    request.session.set_expiry(0) #设置过期时间
    return redirect('/booktest/session1/')
#删除session
def session3(request):
    del request.session['my_name']
    return redirect('/booktest/session1/')