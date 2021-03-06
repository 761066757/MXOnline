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
from apps.operations.views import IndexView

from django.conf.urls import url
from django.conf.urls import include
from django.views.static import serve
from MXOnline.settings import MEDIA_ROOT
from apps.courses.views import CourseLessonView
from apps.users.views import LoginView, LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    # path('', views.index),
    # zheyang就不用定义视图函数
    # path('',TemplateView.as_view(template_name="index.html"),name='index'),
    path('',IndexView.as_view(),name='index'),

    # path('courselist/',TemplateView.as_view(template_name="course-list.html"),name='course-list'),
    # path('login/',LoginView.as_view())
    path('login/',LoginView.as_view(),name='login'),

    #     配置机构展示列表
    # path('orglist/', OrgView.as_view(), name='org_list'),

    # 授课机构相关操作
    url(r'^org/', include(('apps.organizations.urls',"organizations") , namespace='org')),
    # 配置课程相关页面
    url(r'^course/', include(('apps.courses.urls',"courses") , namespace='course')),
    # 配置上传文件的访问url
    url(r'^media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT}),
    # 用户相关操作
    url(r'^op/', include(('apps.operations.urls', "operations"), namespace="op")),
    path('logout/', LogoutView.as_view(), name="logout"),

    url(r'^users/', include(('apps.users.urls', 'users'), namespace='users')),
]

