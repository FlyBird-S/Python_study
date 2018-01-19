from django.urls import path,re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('index/', views.index),
    #path('page/',  views.article_page1),
    #re_path(r'^page/(?P<article_id>[0-9]+)', views.article_page)
    re_path(r'^page/(?P<article_id>[0-9]+)/$', views.article_page,name='page'),
    re_path(r'^edit/(?P<article_id>[0-9]+)/$',views.edit_page,name='edit_page'),
    re_path(r'^edit/action/$',views.edit_action,name='edit_action'),
]

