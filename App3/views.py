from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import datetime
from django.views.decorators.csrf import csrf_exempt
from App3.models import User3
import random

def models(req):
    arr=[
        {
            'name':'增删改',
            'url':'App3:curd'
        },
        {
            'name':'查询',
            'url':'App3:query'
        },
        {
            'name':'查询单个',
            'url':'App3:query_one'
        },
        {
            'name':'分组',
            'url':'App3:group'
        },
        {
            'name':'原生sql',
            'url':'App3:raw'
        },
    ]
    num=100
    return render(
        req,
        'models.html',
        locals()
    )
def raw(req):
    print('*'*100) 
    # data=User3.objects.raw("select * from user3")
    # data=User3.objects.raw("SELECT sex,COUNT(uid) FROM user3 GROUP BY sex")

    username="adsad' or '1"
    # sql="select * from user3 where username='{}'".format(username)
    # data=User3.objects.raw(sql)

    #下面这张写法可以防止sql注入
    # sql="select * from user3 where username=%s"
    # data=User3.objects.raw(sql,[username])

    #自定义sql
    from App3.tools import query
    # data=query("select * from user3")#不传参数
    data=query("select * from user3 where uid=%s",100)#传参数

    print(data)
    return HttpResponse('raw')
    # return render(req,'query.html',locals())



def group(req):
    from django.db.models import Max,Min,Avg,Count
    print('*'*100) 
    # data=User3.objects.values('sex').annotate(Count('uid')).filter(sex=1)
    # print(data)
    return HttpResponse('分组')
def query_one(req):
    data=User3.objects.get(uid=60)
    data=[data]
    return render(req,'query.html',locals())
def query(req):
    #获取所有数据 返回列表
    data=User3.objects.all()
    #根据字段名称查询 返回列表  相当于sql  select * from user3 where uid=5
    # data=User3.objects.filter(uid=30)#查询uid=30的
    # data=User3.objects.filter(uid__gt=30)#查询uid>=30的
    # data=User3.objects.filter(uid__lt=30)#查询uid<40的
    # data=User3.objects.filter(uid__gt=30).filter(uid__lt=40)#可以链式调用 多次过滤

    #排序
    # data=data.order_by('username')#升序
    # data=data.order_by('-username')#反序 字段名前面加一个横线
    # data=data.order_by('username')[:2]#返回值是一个集合，可以进行切片处理
    # data=data.order_by('username')[5:9]#可以进行切片处理

    #取指定字段
    # data=data.values('username','password') 

    #去重
    # data=data.distinct()

    #is null 返回选定字典是否为空的
    data=data.filter(sex__isnull=True)

    print(data)


    return render(req,'query.html',locals())










def curd(req):
    #增加
    # newUser=User3(username='mep1',password='1234561')
    # newUser.save()
    # 快捷增加 这个不需要保存直接创建成功
    # user={'username':'快捷增加','password':'mima33333'}
    # User3.objects.create(**user)
    # 批量创建
    # User3.objects.bulk_create([
    #     User3(username='批量创建3',password='1231423'),
    #     User3(username='批量创建4',password='12314231'),
    #     User3(username='批量创建5',password='12312123'),
    # ])

    familyName=['赵','李','孙','王','张','公孙','慕容']
    lastName=['一','二','三','大','小','二狗','小翠']
    users=[]
    for name in range(100):
        username=familyName[random.randint(0,6)]+lastName[random.randint(0,6)]+str(random.randint(0,600))
        users.append(User3(username=username,password=random.randint(100000,1000000)))
    User3.objects.bulk_create(users)
    # 修改
    # user=User3.objects.get(pk=1) #pk是根据主键进行查找
    # user.password='123000'
    # user.save()

    # 删除
    # try:
    #     user=User3.objects.get(pk=1)
    #     if user:
    #         user.delete()
    # except Exception as e:
    #     print(e)
    # 批量删除
    # users=User3.objects.filter(uid__gte=20)#查找到uid大于等于20的数据
    # users.delete()#全部删除




    return HttpResponse('增删改')

# Create your views here.
