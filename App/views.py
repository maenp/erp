from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from App.models import User
from django.urls import reverse
# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def home(request):
    users=User.objects.all() #查询数据库数据
    return render(request,"home.html",
    context={
        'title':'Django',
        'name':'mep',
        'users':users
    })
def num(request,num):
    print(num)
    return HttpResponse(str(num))
def list(request,name):
    print(name)
    return HttpResponse(str(name))
def path(request,path):
    print(path)
    return HttpResponse(str(path))
def tel(request,tel):
    print(tel)
    return HttpResponse(str(tel))
def change(request,name):
    print('*'*20)
    # GET 传参获取
    # 获取单一值  change/?username=maenping
    # print(request.GET.get('username')) # maenping
    # 获取列表    change/?age=18&age=100
    # print(request.GET.getlist('age')) # ['18', '100']

    # POST 传参获取
    # print(request.POST.get('username'))
    # print(request.POST.getlist('age'))
 
    # 获取请求方法 GET|POST
    # print(request.method)

    # 获取请求路径
    # print(request.path) #/change/

    # 其他
    # print(request.META)
    print(request.META.get('HTTP_REFERER')) #来源页面
    print(request.META.get('REMOTE_ADDR'))  #客户端IP
    print(request.META.get('REMOTE_HOST'))  #客户端主机

    # 常用的方法
    print(request.get_full_path()) #/change/?username=maenping&age=18&age=100
    print(request.get_host()) #localhost:8000
    print(request.build_absolute_uri()) #http://localhost:8000/change/?username=maenping&age=18&age=100

    # 获取请求参数的字典 QueryDict=>dict
    print(request.GET.dict()) # {'username': 'maenping', 'age': '100'}

    print('*'*20)
    return HttpResponse(name)

# 字符串
# def handler(request):
#     res=HttpResponse('响应对象')
#     res.content_type='text/html'
#     res.status_code=201 #可以人为设置状态码
#     return res

# 返回html文件
# def handler(request):
#     res=render(request,'custom.html')
#     return res

# 返回json字符串 JsonResponse其实就是HttpResponse只是参数会自动转为json串
def handler(request):
    #返回字典
    # return JsonResponse({'aaa':111})
    #返回列表  必须传safe=False
    # 字典、列表只能包含内置类型
    return JsonResponse([1,1,2,5,74,10],safe=False)

def redirect(req):
    # 重定向 参数就是路由
    # return HttpResponseRedirect('/handler')
    # return HttpResponseRedirect('https://www.baidu.com/')
    # redirect是HttpResponseRedirect的简写方式
    # return redirect('/handler')
    print('*'*50)
    # 反向对位：由应用命名空间:name来确定路由 
    # res=reverse("App:home")                     #不带参数

    # res=reverse("App:change",args=['redirect']) #带参数 不指定参数名 
    # 参数以列表或元组的方式传递 
    # 如果是以元组方式传递一个参数 后面要加个逗号 如下：
    # res=reverse("App:change",args=('redirect',))

    res=reverse("App:list",kwargs={'name':'maenping'})#带参数 指定参数名 
    # 参数以字典方式传递
    print(res) #带参数

    # print(1 / 0) #服务器会报错
    return HttpResponseRedirect(res)