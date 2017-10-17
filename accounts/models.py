# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class Account(models.Model):
    display_name = models.CharField(max_length=128,verbose_name=u'姓名')
    biography = models.TextField(null=True, blank=True,verbose_name=u'档案')
    homepage = models.URLField(null=True, blank=True,verbose_name=u'主页')
    weixin = models.URLField(null=True, blank=True,verbose_name=u'微信')
    weibo = models.URLField(null=True, blank=True,verbose_name=u'微博')
    user = models.OneToOneField(User)

    @receiver(post_save, sender=User)
    def create_user_account(sender, instance=None, created=False, **kwargs):
        if created:
            Account.objects.get_or_create(user=instance, defaults={'display_name':instance.username})

    def __str__(self):
        return self.display_name