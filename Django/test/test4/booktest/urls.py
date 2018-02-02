from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'(?P<id>\d+)/', views.show, name='show'),
    path('base', views.base, name='base'),
    path('index2', views.index2, name='index2'),
    path('user1', views.user1, name='user1'),
    path('user2', views.user2, name='user2'),
    path('htmlTest', views.htmlTest, name='htmlTest'),
    path('csrf1', views.csrf1, name='csrf1'),
    path('csrf2', views.csrf2, name='csrf2'),
path('verifyCode', views.verifyCode, name='verifyCode'),
path('verifyTest', views.verifyTest, name='verifyTest'),
path('verifyTest2', views.verifyTest2, name='verifyTest2'),

]
