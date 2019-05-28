from django.db import models
from django.contrib.auth.models import AbstractUser, User


# Create your models here.

# 用户表
class MyUser(User):
    # 与choices配合使用
    GENDER_CHOICES = (
        ('M', '男'),
        ('F', '女'),
    )
    nickname = models.CharField(blank=True, null=True, max_length=30, verbose_name='用户昵称')
    avatar = models.FileField(upload_to='avatar/', verbose_name='用户头像')
    mobile = models.CharField(blank=True, null=True, max_length=13, verbose_name='手机号')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True, verbose_name='用户性别')
    subscribe = models.BooleanField(default=False, verbose_name='是否订阅')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        db_table = 'my_user'
