from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """
    用户管理
    """
    user_id = models.AutoField(primary_key=True, null=False)
    token = models.CharField(max_length=200, null=True, default=None)
    nickname = models.CharField(max_length=200, null=True, default=None, verbose_name='用户昵称')
    role = models.ForeignKey('Role', default=1, on_delete=models.CASCADE)
    last_login_ip = models.CharField(max_length=50, null=True, default=None, verbose_name='最后登录IP')
    login_count = models.IntegerField(null=True, default=0, verbose_name='不同ip登录统计')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    ac_token = models.CharField(max_length=100, null=True, default=None, verbose_name='actoken')
    phone = models.CharField(max_length=30, null=True, default=None, verbose_name='手机号')

    def __str__(self):
        return self.username


class Role(models.Model):
    """
    用户角色表
    """
    role_id = models.AutoField(primary_key=True, null=False)
    role_name = models.CharField(max_length=50, null=True, default=True)


class Books(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30, blank=True, null=True)
