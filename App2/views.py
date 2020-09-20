from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import datetime
from django.views.decorators.csrf import csrf_exempt


from django.template import loader #导入loader
# Create your views here.
def temp(req):
    html="""
    <html>
    <body>
    <ul>
     """
    html2="""
    </ul>
    </body>
    </html>
    """
    list=["模板文件展示111","模板文件展示222"]
    for item in list:
        html+="<li>"+item+"</li>"
    html+=html2
    return HttpResponse(html)

def temp(req):
    # 1、加载模板文件，生成模板对象
    obj=loader.get_template("App2/temp.html")
    # 2、模板对象渲染的结果是html源文件（字符串）
    res=obj.render({"list":["模板文件展示111","模板文件展示222"]})
    print(res)
    return HttpResponse(res)

def temp(req):
    res=render(
        req,
        'App2/temp.html',
        context={
            "list":["模板文件展示111","模板文件展示222","模板文件展示333"]}
    )
    return HttpResponse(res)
#--------------------------------------------------------
def var(req):
    num=100
    str='这是一个字符串'
    arr=['乔丹','科比','贝克汉姆','李宁']
    obj={'name':'姚明','age':'35'}
    tel=None
    date=datetime.datetime.now()
    dom="<h1>转义标题</h1>"
    return render(
        req,
        "App2/变量.html",
        locals()
    )

# @csrf_exempt
def register(req):
    if req.method=="POST":
        username=req.POST.get("username")
        password=req.POST.get("password")
        token=req.POST.get("csrfmiddlewaretoken")
        print('*'*50)
        print(username,password)
        print('*'*50)
        print(token)
        print('*'*50)
        res='注册成功'
        return JsonResponse({"code":0,"msg":'注册成功'})
    

    return render(req,"App2/注册.html")

def inclute(req):
    return render(req,"App2/inclute.html")