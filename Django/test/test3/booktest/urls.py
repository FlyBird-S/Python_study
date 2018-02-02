from django.urls import path,re_path
from . import views
urlpatterns = [
        path('index/',views.index,name='index'),
    re_path(r'^(?P<num>\d+)/$',views.detail), # url 的正则表达式中有（）时对于函数得接收其匹配值
    path('getTest1/',views.getTest1),
    path('getTest2/',views.getTest2),
    path('getTest3/',views.getTest3),
    path('postTest1/',views.postTest1),
    path('postTest2/',views.postTest2),
    path('cookieTest/',views.cookieTest),
    path('redTest1/', views.redTest1),
    path('redTest2/', views.redTest2),
    path('session1/', views.session1),
    path('session2/', views.session2),
    path('session2_handle/', views.session2_handle),
    path('session3/', views.session3),
]