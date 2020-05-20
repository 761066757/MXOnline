from django.shortcuts import render
from django.views.generic.base import View
from apps.courses.models import Course
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from apps.operations.models import UserFavorite
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.courses.models import Video,CourseResource,CourseTag
from apps.operations.models import UserCourse,CourseComments
# Create your views here.

class CourseListView(View):
    def get(self, request, *args, **kwargs):
        """
        获取课程列表信息
        """
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


class CourseDetailView(View):
    def get(self, request, course_id, *args, **kwargs):
        """
        获取课程详情
        """
        # 点击到课程的详情就记录一次,根据id
        course = Course.objects.get(id=int(course_id))
        course.click_nums += 1
        course.save()
        # 获取收藏状态
        has_fav_course = False
        has_fav_org = False
        # 用户是否登录
        if request.user.is_authenticated:
            # 查询用户是否收藏了该课程，如果有，证明用户收藏了这个课
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True
            # 查询用户是否收藏了该课程机构，如果有，证明用户收藏了这个机构
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=2):
                has_fav_org = True
        #
        # # 相关课程推荐
        # # 通过课程的单标签tag做课程的推荐
        # tag = course.tag
        # related_courses = []
        # if tag:
        #     # 过滤掉自己
        #     related_courses = Course.objects.filter(tag=tag).exclude(id__in=[course.id])[:3]

        # 通过CourseTag类进行相关课程推荐
        tags = course.coursetag_set.all()
        # 遍历
        tag_list = [tag.tag for tag in tags]
        courses_tags = CourseTag.objects.filter(tag__in=tag_list).exclude(course__id=course.id)
        related_courses = set()
        for courses_tag in courses_tags:
            related_courses.add(courses_tag.course)

        return render(request, "course-detail.html", {
            "course": course,
            "has_fav_course": has_fav_course,
            "has_fav_org": has_fav_org,
            "related_courses": related_courses
        })
# 课程章节
class CourseLessonView(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self, request, course_id, *args, **kwargs):
        """
        获取课程章节信息
        """
        course = Course.objects.get(id=int(course_id))
        course.click_nums += 1
        course.save()

        # 查询资料信息
        course_resource = CourseResource.objects.filter(course = course)

        # 查询当前用户都学了什么课
        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        # 查询这个用户关联的所有课程
        all_courses = UserCourse.objects.filter(user_id__in=user_ids).order_by("-course__click_nums")
        # 过略掉当前课程
        related_courses = []
        for item in all_courses:
            if item.course.id != course.id:
                related_courses.append(item.course)

        return render(request, "course-video.html", {
            "course": course,
            "course_resource": course_resource,
            "related_courses": related_courses,
        })

#课程评论
class CourseCommentsView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request, course_id, *args, **kwargs):
        course = Course.objects.get(id=int(course_id))
        course.click_nums += 1
        course.save()

        comments = CourseComments.objects.filter(course=course)

        # 查询用户是否已经关联了该课程
        user_courses = UserCourse.objects.filter(user=request.user, course=course)
        if not user_courses:
            user_course = UserCourse(user=request.user, course=course)
            user_course.save()

            course.students += 1
            course.save()

        # 学习过该课程的所有同学
        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        all_courses = UserCourse.objects.filter(user_id__in=user_ids).order_by("-course__click_nums")[:5]
        # related_courses = [user_course.course for user_course in all_courses if user_course.course.id != course.id]
        related_courses = []
        for item in all_courses:
            if item.course.id != course.id:
                related_courses.append(item.course)

        course_resources = CourseResource.objects.filter(course=course)

        return render(request, "course-comment.html", {
            "course": course,
            "course_resources": course_resources,
            "related_courses": related_courses,
            "comments":comments,
        })
