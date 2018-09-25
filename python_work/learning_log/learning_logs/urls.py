"""定义learning_log的URL模式"""

#form django.conf.urls import urls
from django.urls import path

from . import views

urlpatterns = [
    #主页
    path = （'', views.index, name='index'）
]
