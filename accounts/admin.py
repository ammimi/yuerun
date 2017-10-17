# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from accounts.models import Account

# #解决后台不能输入中文的问题
# import sys
# reload(sys)
# sys.setdefaultencoding("utf8")


# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ('display_name','biography','homepage','weixin','user')



admin.site.register(Account,AccountAdmin)