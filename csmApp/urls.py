
from django.urls import path
from django.urls import include
from csmApp import views
app_name="csmApp"  #应用的命名空间 
urlpatterns = [
    path('get_client/',views.get_client,name='get_client'),
    path('add_client/',views.add_client,name='add_client'),
    path('remove_client/',views.remove_client,name='remove_client'),
    path('update_client/',views.update_client,name='update_client'),
]
