from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import datetime
from django.views.decorators.csrf import csrf_exempt
import random
from django.contrib.auth import authenticate,login,logout
from csmApp.models import clientInfo


def get_client(req):

    return JsonResponse({"code":1,"msg":'请使用post请求！！！'})
def add_client(req):

    client=req.POST
    print(client)
    # clientInfo.objects.create(**client)
    return JsonResponse({"code":1,"msg":'请使用post请求！！！'})
def remove_client(req):
    return JsonResponse({"code":1,"msg":'请使用post请求！！！'})
def update_client(req):
    return JsonResponse({"code":1,"msg":'请使用post请求！！！'})