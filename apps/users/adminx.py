# encoding:utf-8
import xadmin
from .models import EmailVerifyRecord, Banner


class UserProfileAdmin(object):
    list_display = ['username', 'email', ]
    search_fields = ['username', 'email', 'mobile']
    list_filter = ['username', 'gender', 'email', 'mobile']


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type']

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'url', 'index', 'add_time']
    list_filter = ['title', 'url', 'index', 'add_time']


# xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
