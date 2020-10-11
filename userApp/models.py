from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username=models.CharField(max_length=20,unique=True,verbose_name='用户名')
    password=models.CharField(max_length=128,verbose_name='密码')
    reqtime=models.DateTimeField(auto_now_add=True,verbose_name='注册时间')
    class Meta:
        db_table='user'
        verbose_name='用户表'

# 继承AbstractUser使用Django用户认证系统，username必须是唯一的 否则会报错
# verbose_name