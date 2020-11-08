from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import datetime
from django.views.decorators.csrf import csrf_exempt
import random
from django.core import serializers
from csmApp.models import clientInfo,supplierInfo,tabsInfo,goodsInfo

# 商品信息---------------------
def remove_goods(req):
    pk=req.POST.get("pk")
    goods=goodsInfo.objects.get(pk=pk)
    if goods:
        goods.delete()
        return JsonResponse({"code":0,"msg":'删除成功~'})
    return JsonResponse({"code":1,"msg":'删除失败~'})
def get_goods(req):
    tab_name=req.GET.get("tab_name")
    print(tab_name)
    data=goodsInfo.objects.filter(uid=req.user.id)
    if tab_name != '全部':
        data=data.filter(tab_key=tab_name)
    data = serializers.serialize("python", data)
    return JsonResponse({"code":0,"obj":data,"msg":'成功'})
def add_goods(req):
    goods={ 
        'goods_name':req.POST.get("goods_name"),
        'remark':req.POST.get("remark"),
        'specification':req.POST.get("specification"),
        'unit':req.POST.get("unit"),
        'sale_price':req.POST.get("sale_price"),
        'buy_price':req.POST.get("buy_price"),
        'tab_key':tabsInfo.objects.get(pk=req.POST.get("tab_pk")),
        'uid':req.user.id,
    }
    try:
        goodsInfo.objects.create(**goods)
        return JsonResponse({"code":0,"msg":'添加成功~'})
    except Exception as e:
        return JsonResponse({"code":1,"msg":str(e)})
def update_goods(req):
    goods={ 
        'goods_name':req.POST.get("goods_name"),
        'remark':req.POST.get("remark"),
        'specification':req.POST.get("specification"),
        'unit':req.POST.get("unit"),
        'sale_price':req.POST.get("sale_price"),
        'buy_price':req.POST.get("buy_price"),
        'tab_key':tabsInfo.objects.get(pk=req.POST.get("tab_pk")),
    }
    try:
        goodsInfo.objects.filter(pk=req.POST.get("pk")).update(**goods)
        return JsonResponse({"code":0,"msg":'修改成功~'})
    except Exception as e:
        return JsonResponse({"code":1,"msg":str(e)})


# 商品标签-------------------------------
def remove_tab(req):
    pk=req.POST.get("pk")
    tab=tabsInfo.objects.get(pk=pk)
    if tab:
        tab.delete()
        return JsonResponse({"code":0,"msg":'删除成功~'})
    return JsonResponse({"code":1,"msg":'删除失败~'})
def get_tabs(req):
    data=tabsInfo.objects.filter(uid=req.user.id)
    data = serializers.serialize("python", data)
    return JsonResponse({"code":0,"obj":data,"msg":'成功'})

def add_tab(req):
    client=req.POST
    print(client)
    client={ 
        'tab_name':req.POST.get("tab_name"),
        'uid':req.user.id,
    }
    tabsInfo.objects.create(**client)
    return JsonResponse({"code":0,"msg":'添加成功~'})

# 客户信息---------------------------
def add_client(req):
    client=req.POST
    print(client)
    client={ 
        'client_name':req.POST.get("client_name"),
        'link_man':req.POST.get("link_man"),
        'link_tel':req.POST.get("link_tel"),
        'uid':req.user.id,
    }
    clientInfo.objects.create(**client)
    return JsonResponse({"code":0,"msg":'添加成功~'})
def remove_client(req):
    pk=req.POST.get("pk")
    client=clientInfo.objects.get(pk=pk)
    if client:
        client.delete()
        return JsonResponse({"code":0,"msg":'删除成功~'})
    return JsonResponse({"code":1,"msg":'删除失败~'})
def get_client(req):
    data=clientInfo.objects.filter(uid=req.user.id)
    data = serializers.serialize("python", data)
    return JsonResponse({"code":0,"obj":data,"msg":'成功'})

# 供应商信息-----------------------------------
def add_supplier(req):
    supplier=req.POST
    print(req)
    supplier={
        'supplier_name':req.POST.get("supplier_name"),
        'link_man':req.POST.get("link_man"),
        'link_tel':req.POST.get("link_tel"),
        'uid':req.user.id,
    }
    supplierInfo.objects.create(**supplier)
    return JsonResponse({"code":0,"msg":'添加成功~'})
def remove_supplier(req):
    pk=req.POST.get("pk")
    supplier=supplierInfo.objects.get(pk=pk)
    if supplier:
        supplier.delete()
        return JsonResponse({"code":0,"msg":'删除成功~'})
    return JsonResponse({"code":1,"msg":'删除失败~'})
def get_supplier(req):
    data=supplierInfo.objects.filter(uid=req.user.id)
    data = serializers.serialize("python", data)
    return JsonResponse({"code":0,"obj":data,"msg":'成功'})


