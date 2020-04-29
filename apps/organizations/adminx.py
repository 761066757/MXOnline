import xadmin
from apps.organizations.models import *
# 不用继承admin.ModelAdmin，
class CityAdmin(object):
    # pass
    # # 显示字典
    list_display = ["id", "name", "city_desc"]
    # # 搜索字段(过滤)
    search_fields = ["name", "city_desc"]
    list_filter = ["id", "name", "city_desc"]
class CourseOrgAdmin(object):
    # pass
    # 显示字典
    list_display = ["id", "city", "name","tag","category"]
    # 搜索字段(过滤)
    search_fields = ["city", "name","tag","category"]
    list_filter = ["id", "city", "name","tag","category"]
class TeacherAdmin(object):
    # pass
    # # 显示字典
    list_display = ["id", "name", "user","courseorg","teach_times"]
    # # 搜索字段(过滤)
    search_fields = ["name", "user","courseorg","teach_times"]
    list_filter = ["id", "name", "user","courseorg","teach_times"]

xadmin.site.register(City, CityAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)