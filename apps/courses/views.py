from django.shortcuts import render
from django.views.generic.base import View
from apps.courses.models import Course
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
class CourseListView(View):
    def get(self, request, *args, **kwargs):
        """获取课程列表信息"""
        all_courses = Course.objects.order_by("-add_time")
        # 获取热门课程前三个
        hot_courses = Course.objects.order_by("-click_nums")[:3]

        # 课程排序
        sort = request.GET.get("sort", "")
        if sort == "students":
            all_courses = all_courses.order_by("-students")
        elif sort == "hot":
            all_courses = all_courses.order_by("-click_nums")


        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, per_page=5, request=request) # 每页显示多少个
        courses = p.page(page)

        return render(request, "course-list.html",
                      {"all_courses": courses,
                       "sort": sort,
                       "hot_courses": hot_courses,
                       })