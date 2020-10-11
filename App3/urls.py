
from django.urls import path
from django.urls import include
from App3 import views
app_name="App3"  #应用的命名空间 
urlpatterns = [
    path('',views.models,name='models'),
    path('curd/',views.curd,name='curd'),
    path('query/',views.query,name='query'),
    path('query_one/',views.query_one,name='query_one'),
    path('group/',views.group,name='group'),
    path('raw/',views.raw,name='raw'),
]
