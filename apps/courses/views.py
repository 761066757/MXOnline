from django.shortcuts import render
from django.views.generic.base import View
from apps.courses.models import Course

# Create your views here.
class CourseListView(View):
    def get(self, request, *args, **kwargs):
        """hu"""