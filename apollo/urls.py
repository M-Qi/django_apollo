from django.urls import path

from apollo import views

urlpatterns = [
    path('login/',views.login),# 配置登录路由
    path('index/',views.index),# 实现首页
    path('sefe/',views.safe_a),# 配置登录路由
]
