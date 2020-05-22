from django.conf.urls import url
from apps.organizations.views import OrgView
from apps.organizations.views import OrgView, AddAsk,TeacherListView,TeacherDetailView

urlpatterns = [
    url(r'^list/$',OrgView.as_view(), name="list"),
    url(r'^add_ask/$',AddAsk.as_view(), name="add_ask"),
    # 教师相关
    url(r'^teachers/$',TeacherListView.as_view(), name="teachers"),
    url(r'^teachers/(?P<teacher_id>\d+)$',TeacherDetailView.as_view(), name="teacher_detail"),
]