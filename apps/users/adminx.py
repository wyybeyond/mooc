# encoding:utf-8
import xadmin
from .models import EmailVerifyRecord, Banner
from xadmin import views


class UserProfileAdmin(object):
    list_display = ['username', 'email', ]
    search_fields = ['username', 'email', 'mobile']
    list_filter = ['username', 'gender', 'email', 'mobile']


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'url', 'index', 'add_time']
    list_filter = ['title', 'url', 'index', 'add_time']


# 使用Xadmin的主题功能
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


# Xadmin全局配置参数信息设置

class GlobalSettings(object):
    site_title = '慕课网后台管理系统'
    site_footer = '慕课在线网'

    # 收起菜单
    menu_style = 'accordion'

    # def get_site_menu(self):
    #     return (
    #         {'title': '课程管理', 'menus': (
    #             {'title': '课程信息', 'url': self.get_model_url(Course, 'changelist')},
    #             # {'title': '章节信息', 'url': self.get_model_url(Lesson, 'changelist')},
    #             # {'title': '视频信息', 'url': self.get_model_url(Video, 'changelist')},
    #             # {'title': '课程资源', 'url': self.get_model_url(CourseResource, 'changelist')},
    #             # {'title': '课程评论', 'url': self.get_model_url(CourseComments, 'changelist')},
    #         )},
    #         {'title': '机构管理', 'menus': (
    #             # {'title': '所在城市', 'url': self.get_model_url(CityDict, 'changelist')},
    #             # {'title': '机构讲师', 'url': self.get_model_url(Teacher, 'changelist')},
    #             # {'title': '机构信息', 'url': self.get_model_url(CourseOrg, 'changelist')},
    #         )},
    #         {'title': '用户管理', 'menus': (
    #             # {'title': '用户信息', 'url': self.get_model_url(UserProfile, 'changelist')},
    #             # {'title': '用户验证', 'url': self.get_model_url(EmailVerifyRecord, 'changelist')},
    #             # {'title': '用户课程', 'url': self.get_model_url(UserCourse, 'changelist')},
    #             # {'title': '用户收藏', 'url': self.get_model_url(UserFavorite, 'changelist')},
    #             # {'title': '用户消息', 'url': self.get_model_url(UserMessage, 'changelist')},
    #         )},
    #         {'title': '系统管理', 'menus': (
    #             # {'title': '用户咨询', 'url': self.get_model_url(UserAsk, 'changelist')},
    #             # {'title': '首页轮播', 'url': self.get_model_url(Banner, 'changelist')},
    #             # {'title': '用户分组', 'url': self.get_model_url(Group, 'changelist')},
    #             # {'title': '用户权限', 'url': self.get_model_url(Permission, 'changelist')},
    #             # {'title': '日志记录', 'url': self.get_model_url(Log, 'changelist')},
    #         )},
    #     )


# xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
