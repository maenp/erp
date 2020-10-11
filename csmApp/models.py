from django.db import models

# Create your models here.
class clientInfo(models.Model):
    client_name=models.CharField(max_length=50,verbose_name='客户名称')
    link_man=models.CharField(max_length=10,verbose_name='联系人')
    link_tel=models.CharField(max_length=12,verbose_name='联系电话')
    delivery_day=models.DateTimeField(max_length=128,verbose_name='交货时间')
    delivery_site=models.CharField(max_length=128,verbose_name='交货地址')
    uid=models.IntegerField(default=10)
    class Meta:
        db_table='client_info'
        verbose_name='客户表'
