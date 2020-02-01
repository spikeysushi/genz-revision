from django.shortcuts import render, redirect
from .models import Shop, Item
from  .forms import ItemForm, ShopForm


# Create your views here.

def shop_list(request):
    context = {
        "shops": Shop.objects.all()
    }
    return render(request, 'shop.html', context)

def item_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, 'item.html', context)

def shop_create(request):
    form = ShopForm()
    if request.method == "POST":
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop')
    context = {
        "form":form,
    }
    return render(request, 'shop_create.html', context)

def item_create(request):
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item')
    context = {
        "form":form,
    }
    return render(request, 'item_create.html', context)