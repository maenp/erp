from django.contrib import admin

# Register your models here.
from csmApp.models import clientInfo,supplierInfo,tabsInfo,goodsInfo

class GoodsAdmin(admin.ModelAdmin):
    #显示的字段
    list_display=['pk','goods_name','remark','tab_key','specification','unit','sale_price','buy_price','create_time']
    #搜索字段
    search_fields=['goods_name']

admin.site.register(goodsInfo,GoodsAdmin)
