from django.urls import path

from apollo import views

urlpatterns = [
    path('login/',views.login),# 配置登录路由
    path('index/',views.index),# 实现首页
    path('sefe/',views.safe_a),# 配置登录路由
    path('safe_b/',views.safe_b),# 实现B安全等级的路由
    path('reg/',views.reg),# 实现注册功能的路由
    path('safe_c/',views.safe_c),# 实现C安全等级的路由

]
