    
from django.contrib import admin
from .models import Shop, Item

# Register your models here.


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id','name','address']
    list_display_links = ['name']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id','name','desc','price']
    list_display_links = ['name']
    list_filter = ["created_at"]