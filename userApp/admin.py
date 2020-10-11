from django.contrib import admin

# Register your models here.
from userApp.models import User

class UserAdmin(admin.ModelAdmin):
    #显示的字段
    list_display=['pk','username','password']
    #搜索字段
    search_fields=['username']

admin.site.register(User,UserAdmin)