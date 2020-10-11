
from django.urls import path
from django.urls import include
from App2 import views
app_name="App2"  #应用的命名空间 
urlpatterns = [
    path('temp/',views.temp,name='temp'),
    path('var/',views.var,name='var'),
    path('register/',views.register,name='register'),
    path('inclute/',views.inclute,name='inclute'),
    path('static/',views.static,name='static'),
    path('jinja2/',views.jinja2,name='jinja2'),

]
