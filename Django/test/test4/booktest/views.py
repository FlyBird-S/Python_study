from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def index(request):
    hero = HeroInfo.objects.get(pk=1)
    # hero_list = HeroInfo.objects.all().filter(isDelete=True)
    hero_list = HeroInfo.objects.all()
    context = {'hero': hero, 'hero_list': hero_list}
    return render(request, 'booktest/index.html', context)


def show(request, id):
    context = {'id': id}
    return render(request, 'booktest/show.html', context)


# 模版继承
def base(request):
    return render(request, 'booktest/base.html')


def index2(request):
    return render(request, 'booktest/index2.html')


def user1(request):
    return render(request, 'booktest/user1.html')


def user2(request):
    return render(request, 'booktest/user2.html')


# html 转义
def htmlTest(request):
    context = {"t1": "<h1>123</h1>"}
    return render(request, 'booktest/htmlTest.html', context)


# csrf
def csrf1(request):
    return render(request, 'booktest/csrf1.html')


def csrf2(request):
    uname = request.POST.get('uname')
    return HttpResponse(uname)


# 验证码
def verifyCode(request):
    from PIL import Image, ImageDraw, ImageFont
    import random
    # 创建背景色
    bgColor = (random.randrange(5, 255), random.randrange(5, 255), random.randrange(5, 255))
    width = 100
    height = 25
    # 创建画布
    image = Image.new('RGB', (width, height), bgColor)
    # 创建字体
    font = ImageFont.truetype('FreeMono.ttf', 23)  # usr/share/fonts/truetype/freefpmt
    # 创建画笔
    draw = ImageDraw.Draw(image)
    # 创建文本内容
    text = '012356789QWERTYUIOPASDFGHJKLZXCVBNM'
    # draw.text((0,0),text,(255,255,255),font)
    Text_values = ''
    for i in range(4):
        text_buf = text[random.randrange(0, len(text))]
        Text_values += text_buf
        draw.text(
            (i * 25, 0), text_buf, (255, 255, 255), font
        )
    request.session['code'] = Text_values
    from io import BytesIO  # io流
    buf = BytesIO()
    image.save(buf, 'png')
    print(Text_values)
    # 将内存流中内容输出
    return HttpResponse(buf.getvalue(), 'image/png')

def verifyTest(request):
    return render(request,'booktest/verifyTest.html')

def verifyTest2(request):
    in_code = request.POST.get('verify_code')
    if in_code == request.session.get('code'):
        return HttpResponse('ok')
    else:
        return HttpResponse('No')