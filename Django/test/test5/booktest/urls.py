from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='img'),
    path('mid',views.myexc)
]