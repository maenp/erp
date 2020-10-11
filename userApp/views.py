from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import datetime
from django.views.decorators.csrf import csrf_exempt
# from App3.models import User3
import random
from django.contrib.auth import authenticate,login,logout
from userApp.forms import ReqisterForm
from userApp.models import User


#使用Django认证系统加密注册
@csrf_exempt
def register(req):
    if req.method=="POST":
        is_staff=req.POST.get("is_staff")
        print(is_staff)
        form=ReqisterForm(req.POST)
        if form.is_valid():
            data=form.cleaned_data
            print(data)
            data.pop('confirm')
            print(data)
            # return JsonResponse({"code":0,"msg":'注册成功'})
            # res=User.objects.create(**data)    #普通注册到数据库
            res=User.objects.create_user(**data) #使用Django认证系统加密注册
            if res:
                return JsonResponse({"code":0,"msg":'注册成功'})
        print(form._errors)
        return JsonResponse({"code":1,"msg":str(form._errors)})
    return JsonResponse({"code":1,"msg":'请使用post请求！！！'})
@csrf_exempt
def _login(req):
    if req.method=="GET":
        return JsonResponse({"code":1,"msg":'请使用post请求！！！'})
    username=req.POST.get("username","")
    password=req.POST.get("password","")

    #用户验证 验证成功返回user对象 否则返回none
    user= authenticate(req,username=username,password=password)
    print(user,'查找对象')
    if user:
        login(req,user)#记录用户登录状态，参数
        return JsonResponse({
            "code":0,
            "obj":{
                'username':user.username,
                'id':user.id
            },
            "msg":'登录成功'
            })
    return JsonResponse({"code":1,"msg":'登录失败'})
#登出
def _logout(req):
    is_login_status=req.user.is_authenticated
    if is_login_status:
        logout(req)
        return JsonResponse({"code":0,"msg":'退出登录成功'})
    return JsonResponse({"code":1,"msg":'当前状态未登录'})

#判断是否登录
def is_login(req):
    is_login_status=req.user.is_authenticated
    print(req.user.id)
    return JsonResponse({"code":0,"msg":is_login_status})
    
#修改密码
def change_password(req):
    if req.method=="GET":
        return JsonResponse({"code":1,"msg":'请使用post请求！！！'})
    print(req.POST)
    id=req.POST.get("id","")

    user=User.objects.get(pk=id)
    if user:
        password=req.POST.get("password","")
        user.set_password(password)
        user.save()
        return JsonResponse({"code":0,"msg":'修改成功'})

