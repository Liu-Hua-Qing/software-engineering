"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from accounts import views

from accounts import views as accounts_views  # 导入 accounts 

urlpatterns = [
    path('', accounts_views.login_view, name='home'),  # 根路径路由到登录页面
    path('login/', views.login_view, name='login'),  # 登录页面路由
    path('register/', views.register_view, name='register'),  # 注册页面路由
    path('system/', views.system_view, name='system'),  # 注册页面路由
    path('usersystem/', views.usersystem_view, name='usersystem'),
    path('main_info/', views.main_info_view, name='主要信息'),
    path('underwater_system/', views.underwater_system_view, name='水下系统'),
    path('data_center/', views.data_center_view, name='数据中心'),
    path('smart_center/', views.smart_center_view, name='智能中心'),
    path('admin_management/', views.admin_management_view, name='管理员管理'),
    # 其他路由...
]

