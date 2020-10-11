
from django.urls import path
from django.urls import include
from userApp import views
app_name="userApp"  #应用的命名空间 
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views._login,name='login'),
    path('logout/',views._logout,name='logout'),
    path('is_login/',views.is_login,name='is_login'),
    path('change_password/',views.change_password,name='change_password'),
]
