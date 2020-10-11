from django.db import models

# Create your models here.
#自定义模型必须继承Models
class User3(models.Model):
    #字段名不能是关键字；不能使用连续的下划线；
    #db_column:数据库表中的字段名称
    # uid=models.AutoField(primary_key=True,db_column='userid')
    uid=models.AutoField(primary_key=True)
    #CharField类型必须指明长度max_length
    username=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=128)
    #创建时自动记录时间
    reqtime=models.DateTimeField(auto_now_add=True)
    sex=models.IntegerField()

    class Meta: # 元数据，描述这个模型本身的信息
        db_table='user3' #表名 默认：应用名_模型名
        ordering=['username'] #根据username字段排序 默认根据主键排序