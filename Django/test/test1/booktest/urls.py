from django.urls import path
from django.urls import re_path

from . import views
urlpatterns = [
    path('',views.index),
    path('index/',views.index),# 从目录找函数  url->view->templates
    re_path(r'^(\d+)$',views.show),
]
