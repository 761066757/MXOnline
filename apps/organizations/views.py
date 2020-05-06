from django.shortcuts import render
from django.views.generic import View
from apps.organizations.models import CourseOrg,City,Teacher
# Create your views here.

class OrgView(View):
    def get(self, request, *args, **kwargs):
        """
            展示
            :param request:
            :param args:
            :param kwargs:
            :return:
        """
        all_orgs = CourseOrg.objects.all()
        all_nums = CourseOrg.objects.all().count()
        all_city = City.objects.all().count()


        # return render(request, 'org-list.html')
        return render(request, 'org-list.html',{'all_orgs': all_orgs,})