from django.shortcuts import render
from .models import Shop, Item

def shop_list(request):
    # DB로부터 Shop목록을 Fetch할 예정
    qs = Shop.objects.all() # QuerySet 타입

    return render(request, 'shop/shop_list.html', {
    'shop_list': qs,
    })

def shop_detail(request, pk):
    shop = Shop.objects.get(pk=pk)
    return render(request, 'shop/shop_detail.html', {
        'shop': shop,
    })

def item_list(request):
    # DB로부터 Item목록을 Fetch할 예정
    qs = Item.objects.all() # QuerySet 타입

    return render(request, 'shop/item_list.html', {
    'item_list': qs,
    })

def item_detail(request, pk):
    item = Item.objects.get(pk=pk)
    return render(request, 'shop/item_detail.html', {
        'item': item,
    })