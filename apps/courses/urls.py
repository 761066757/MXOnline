from django.conf.urls import url
from apps.courses.views import CourseListView
from apps.courses.views import  CourseDetailView,CourseLessonView

urlpatterns = [
    url(r'^list/$',CourseListView.as_view(), name="list"),
    # url(r'^detail/$',CourseListView.as_view(), name="detail"),
    url(r'^(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="detail"),
    url(r'^(?P<course_id>\d+)/lesson$', CourseLessonView.as_view(), name="lesson"),
]

