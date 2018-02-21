from django.contrib import admin
from .models import UserProfile


# 写一个用户的管理器，采用mode+Admin的命名方式
class UserProfileAdmin(admin.ModelAdmin):
    pass


# 将UserProfile注册到admin中
admin.site.register(UserProfile, UserProfileAdmin)
