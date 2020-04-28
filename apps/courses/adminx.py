import xadmin
from apps.courses.models import Course
# 不用继承admin.ModelAdmin，
class CourseAdmin(object):
    # pass
    # 显示字典
    list_display = ["id", "name", "desc", "learn_times", "degree"]
    # 搜索字段(过滤)
    search_fields = ["name", "desc","learn_times"]
    list_filter = ["id", "name", "desc", "learn_times", "degree"]

xadmin.site.register(Course, CourseAdmin)