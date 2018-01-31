from django.urls import path,re_path
from . import views
urlpatterns = [
        path('index/',views.index,name='index'),
    re_path(r'^(?P<num>\d+)/$',views.detail), # url 的正则表达式中有（）时对于函数得接收其匹配值
    path('getTest1/',views.getTest1),
    path('getTest2/',views.getTest2),
    path('getTest3/',views.getTest3),
]