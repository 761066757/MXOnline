"""MXOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import xadmin
from apps.users import views
from django.views.generic import  TemplateView
from apps.users.views import LoginView
from apps.organizations.views import OrgView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    # path('', views.index),
    # zheyang就不用定义视图函数
    # path('',TemplateView.as_view(template_name="index.html")),
    path('',TemplateView.as_view(template_name="index.html"),name='index'),
    # path('login/',LoginView.as_view())
    path('login/',LoginView.as_view(),name='login'),
#     配置机构展示列表
    path('orglist/', OrgView.as_view(), name='org_list')

]
