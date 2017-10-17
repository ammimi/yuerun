#!/usr/bin/env python
#-*- coding:utf-8 -*-

from rest_framework import serializers
from accounts.models import Account
from django.contrib.auth import get_user_model

class AccountSerializers(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Account
        field = ('id','display_name','biography','homepage','weixin',)

    def create(self, validated_data):
        return Account.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('display_name', instance.display_name)
        instance.code = validated_data.get('biography', instance.biography)
        instance.linenos = validated_data.get('homepage', instance.homepage)
        instance.language = validated_data.get('weixin', instance.weixin)
        instance.save()
        return instance