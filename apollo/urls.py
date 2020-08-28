from django.urls import path

from apollo import views

urlpatterns = [
    path('login/',views.login),# 配置登录路由
]
