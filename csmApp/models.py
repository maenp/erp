from django.db import models

# Create your models here.
class clientInfo(models.Model):
    client_name=models.CharField(unique=True,max_length=50,verbose_name='客户名称')
    link_man=models.CharField(max_length=10,verbose_name='联系人')
    link_tel=models.CharField(max_length=12,verbose_name='联系电话')
    # delivery_day=models.DateTimeField(max_length=128,verbose_name='交货时间')
    # delivery_site=models.CharField(max_length=128,verbose_name='交货地址')
    key = models.IntegerField(auto_created=True,default=1)
    uid=models.IntegerField(default=10)
    class Meta:
        db_table='client_info'
        verbose_name='客户表'

class supplierInfo(models.Model):
    supplier_name=models.CharField(max_length=50,verbose_name='供应商名称')
    link_man=models.CharField(max_length=10,verbose_name='联系人')
    link_tel=models.CharField(max_length=12,verbose_name='联系电话')
    key = models.IntegerField(auto_created=True,default=1)
    uid=models.IntegerField(default=10)
    class Meta:
        db_table='supplier_info'
        verbose_name='供应商表' 


class tabsInfo(models.Model):
    tab_name=models.CharField(unique=True,max_length=10,verbose_name='标签名称')
    uid=models.IntegerField(default=10)
    def __str__(self):
        return self.tab_name
    class Meta:
        db_table='tabs_info'
        verbose_name='标签类目表'


class goodsInfo(models.Model):
    goods_name=models.CharField(max_length=10,verbose_name='商品名称')
        # null=True 创建一条新记录时,该字段可不填,数据库会用默认值NULL填充
        # blank=True 创建数据库记录时该字段可传空白(空串,空字符串)
    sale_price=models.FloatField(verbose_name='销售价格')
    buy_price=models.FloatField(null=True, blank=True,verbose_name='采购价格')
    unit=models.CharField(max_length=5,verbose_name='单位')
    #使用ForeignKey创建外键 一对多
    #models.CASCADE -> 当tabsInfo表中的某个数据被删除,那么goodsInfo表中的对应的数据也会删除(级联删除)
    tab_key = models.ForeignKey('tabsInfo',to_field='tab_name',on_delete=models.CASCADE,verbose_name='分类')
    specification=models.CharField(max_length=20,null=True, blank=True,verbose_name='规格/型号')
    remark=models.TextField(null=True, blank=True,verbose_name='备注')


    uid=models.IntegerField(default=10)
    create_time=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='goods_info'
        verbose_name='商品表'


class orderGoodsInfo(models.Model):
    goods = models.ForeignKey('goodsInfo',on_delete=models.CASCADE,verbose_name='商品')
    order_id=models.IntegerField(verbose_name='销售单号')
    sale_num=models.IntegerField(verbose_name='销售数量')
    class Meta:
        db_table='orderGoods_info'
        verbose_name='订单商品表'

class orderInfo(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='销售单号')

    sale_date=models.DateField(verbose_name='销售日期')

    client =models.CharField(max_length=50,verbose_name='客户')
    client_man =models.CharField(null=True, blank=True,max_length=50,verbose_name='联系人')
    client_tel = models.CharField(null=True, blank=True,max_length=11,verbose_name='联系电话')

    delivery_site=models.CharField(max_length=100,verbose_name='交货地址')
    delivery_date=models.DateField(verbose_name='交货日期')
    total_price=models.FloatField(verbose_name='总金额')
    order_finish=models.BooleanField(default=False,verbose_name='订单完成状态')

    remark=models.TextField(null=True, blank=True,verbose_name='备注')
    sale=models.CharField(null=True, blank=True,max_length=50,verbose_name='销售方')
    sale_man=models.CharField(null=True, blank=True,max_length=50,verbose_name='销售员')
    sale_tel=models.CharField(null=True, blank=True,max_length=50,verbose_name='联系电话')


    uid=models.IntegerField(default=10)
    create_time=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='order_info'
        verbose_name='订单表'


