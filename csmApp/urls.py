
from django.urls import path
from django.urls import include
from csmApp import views
app_name="csmApp"  #应用的命名空间 
urlpatterns = [
    path('get_client/',views.get_client,name='get_client'),
    path('add_client/',views.add_client,name='add_client'),
    path('remove_client/',views.remove_client,name='remove_client'),

    path('get_supplier/',views.get_supplier,name='get_supplier'),
    path('add_supplier/',views.add_supplier,name='add_supplier'),
    path('remove_supplier/',views.remove_supplier,name='remove_supplier'),

    path('get_tabs/',views.get_tabs,name='get_tabs'),
    path('add_tab/',views.add_tab,name='add_tab'),
    path('remove_tab/',views.remove_tab,name='remove_tab'),

    path('get_goods/',views.get_goods,name='get_goods'),
    path('add_goods/',views.add_goods,name='add_goods'),
    path('remove_goods/',views.remove_goods,name='remove_goods'),
    path('update_goods/',views.update_goods,name='update_goods'),
]
