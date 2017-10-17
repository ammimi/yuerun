#!/usr/bin/env python
#-*- coding:utf-8 -*-

from rest_framework import serializers
from accounts.models import Account

class AccountSerializers(serializers.Serializer):
    class Meta:
        model = Account
        field = ('id','display_name','biography','homepage','weixin',)

