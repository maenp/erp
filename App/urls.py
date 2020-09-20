from django.urls import path,re_path
from App import views
app_name="App"  #应用的命名空间 
# 路由列表 名称就叫urlpatterns
urlpatterns=[
    # 不能以 / 开头
    path('home/',views.home,name='home'),
    # string 默认参数类型 常用
    path('change/<name>/',views.change,name='change'),
    #  int 包含 0 和正整数
    path('number/<int:num>/',views.num,name='number'),
    # slug 包含 数字 字母 - _
    path('list/<slug:name>/',views.list,name='list'),
    # path 所有字符串类型 包括 /  
    path('any/<path:path>/',views.path,name='path'),
    # 正则匹配 1开头 11位数字
    re_path(r'^tel/(1\d{10})/$',views.tel,name='tel'),




    path('handler',views.handler,name='handler'),
    path('redirect/',views.redirect,name='redirect')
]

