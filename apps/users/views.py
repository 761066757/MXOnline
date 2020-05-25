from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect
from apps.users.form import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from apps.users.models import UserProfile
from apps.operations.models import UserFavorite
from apps.courses.models import Course
from apps.organizations.models import Teacher,CourseOrg
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))

        next = request.GET.get("next", "")
        return render(request, "login.html", {
            "next": next,
        })

    def post(self, request, *args, **kwargs):
        """
        用户登录验证
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # 实例化 LoginForm
        
        login_form = LoginForm(request.POST)
        if login_form.is_valid():

            # 用于通过用户名和密码查询用户是否存在
            user_name = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=user_name, password=password)
        # 判断user对象是否存在
            if user is not None:
            # 不为空， z证明查询到了用户
                login(request, user)
                # 取一下next值
                # 登录成功之后应该怎么返回页面
                # 先取到next值
                next = request.GET.get("next", "")
                if next:
                    return HttpResponseRedirect(next)

            # 重定向到网站首页
                return HttpResponseRedirect(reverse("index"))
            else:
            # 未查询到用户，要求重新登录,仍然返回login界面
                return render(request, 'login.html',{"msg":"用户名密码错误", "login_form":login_form})
        else:
            return render(request, "login.html", {"login_form":login_form})

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse("index"))

class UserInfoView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, *args, **kwargs):
        current_page = 'info'
        return render(request, 'usercenter-info.html', {
            "current_page":current_page
        })

class MyCourseView(LoginRequiredMixin, View):
    pass


# 用户收藏内容
class MyFavOrgView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        current_page = 'myfavorg'
        fav_orgs = UserFavorite.objects.filter(user=request.user,fav_type = 2)
        org_list = []
        for fav_org in fav_orgs:
            org = CourseOrg.objects.get(id = fav_org.fav_id )
            org_list.append(org)
        return render(request, 'usercenter-fav-org.html', {
            "current_page": current_page,
            "org_list":org_list
        })

class MyFavTeacherView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, *args, **kwargs):
        current_page = 'myfav_teacher'
        fav_teachers = UserFavorite.objects.filter(user=request.user,fav_type = 3)
        teacher_list = []
        for fav_teacher in fav_teachers:
            teacher = Teacher.objects.get(id=fav_teacher.fav_id)
            teacher_list.append(teacher)
        return render(request, 'usercenter-fav-teacher.html', {
            "current_page": current_page,
            "teacher_list": teacher_list,
        })


class MyFavCourseView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, *args, **kwargs):
        current_page = 'myfav_course'
        fav_courses = UserFavorite.objects.filter(user=request.user,fav_type = 1)
        course_list = []
        for fav_course in fav_courses:
            course = Course.objects.get(id=fav_course.fav_id)
            course_list.append(course)
        return render(request, 'usercenter-fav-course.html', {
            "current_page": current_page,
            "course_list": course_list,
        })