from django.contrib import admin
#
# # Register your models here.
#
# from apps.users.models import UserProfile
# class UserprofileAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(UserProfile,UserprofileAdmin)



# 因为用户表相对来说
from apps.users.models import UserProfile
from django.contrib.auth.admin import UserAdmin
admin.site.register(UserProfile, UserAdmin)