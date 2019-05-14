from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Shop, Item
from .forms import ShopForm


def shop_list(request):
    query = request.GET.get('query', '').strip()
    qs = Shop.objects.all()
    if query:
        qs = qs.filter(name__icontains=query)
    return render(request, 'shop/shop_list.html', {
        'shop_list': qs,
        'query': query,
    })

# shop_list = ListView.as_view(model=Shop, paginate_by=20)

def shop_detail(request, pk):
    shop = Shop.objects.get(pk=pk)
    return render(request, 'shop/shop_detail.html', {
        'shop': shop,
    })

# shop_detail = DetailView.as_view(model=Shop)

# def shop_new(request):
#     if request.method == 'POST':  # 'GET', 'POST'
#         # request.GET, request.POST, request.FILES
#         form = ShopForm(request.POST, request.FILES)
#         if form.is_valid():
#             shop = form.save()
#             return redirect('/shop/{}/'.format(shop.pk))
#     else:
#         form = ShopForm()
#     return render(request, 'shop/shop_form.html', {
#         'form': form,
#     })

shop_new = CreateView.as_view(model=Shop, form_class=ShopForm)


def shop_edit(request, pk):
    shop = Shop.objects.get(pk=pk)
    if request.method == 'POST':  # 'GET', 'POST'
        # request.GET, request.POST, request.FILES
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            shop = form.save()
            # return redirect('/shop/{}/'.format(shop.pk))
            return redirect(shop)
    else:
        form = ShopForm(instance=shop)
    return render(request, 'shop/shop_form.html', {
        'form': form,
    })

# shop_edit = UpdateView.as_view(model=Shop, form_class=ShopForm,
#                                success_url='/shop/')


# def shop_delete(request, pk):
#     shop = get_object_or_404(Shop, pk=pk)

#     if request.method == 'POST':
#         shop.delete()
#         return redirect(shop)

#     return render(request, 'shop/shop_confirm_delete.html', {
#         'shop': shop,
#     })

shop_delete = DeleteView.as_view(model=Shop,
                                 success_url=reverse_lazy('shop:shop_list'))

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