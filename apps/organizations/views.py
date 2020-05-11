from django.shortcuts import render
from django.views.generic import View
from apps.organizations.models import CourseOrg, City, Teacher
from django.shortcuts import render_to_response
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from apps.organizations.forms import AddAskForm

# Create your views here.
class OrgView(View):
    def get(self, request, *args, **kwargs):
        """
        展示授课机构列表页
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # 查询机构数量
        all_orgs = CourseOrg.objects.all()
        all_citys = City.objects.all()

        hot_orgs = all_orgs.order_by("-click_nums")[:3]

        # 获取点击的类目
        category = request.GET.get("ct", "")
        if category:
            all_orgs = all_orgs.filter(category=category)

        # 所在城市进行筛选
        city_id = request.GET.get("city", "")
        if city_id:
            if city_id.isdigit():
                all_orgs = all_orgs.filter(city_id=int(city_id))

        # 对机构进行排序
        sort = request.GET.get("sort", "")
        if sort == "students":
            all_orgs = all_orgs.order_by('-students')  # 减号是倒序-学生人数
        elif sort == "courses":
            all_orgs = all_orgs.order_by('-course_nums')  # 减号是倒序-课程数

        # 查询多少家
        org_nums = all_orgs.count()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, per_page=5, request=request) # 每页显示多少个
        orgs = p.page(page)
        return render(request, "org-list.html",
                      { "all_orgs": orgs,
                        "org_nums": org_nums,
                        "all_citys": all_citys,
                        "city_id":city_id,
                        "category":category,
                        "sort":sort,
                        "hot_orgs": hot_orgs,
                        })



class AddAsk(View):
    def post(self, request, *args, **kwargs):
        """
        处理用户的咨询模块
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        userask_form = AddAskForm(request.POST)
        # 如果合法则保存
        if userask_form.is_valid():
            userask_form.save(commit=True)
            return JsonResponse({
                "status": "success",
                 "msg": "提交成功"
            })
        else:
            return JsonResponse({
                "status": "fail",
                "msg": "提交出错"
            })
