from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from app.models import *

def viewmanageorder(request):
    id = request.GET.get('id', '')
    order =  get_object_or_404(Order, id=id)
    print('id order: ')
    print(id)
    order_items = {}
    total = 0
    items = OrderItem.objects.filter(order=order)
    order_items[order] = items
    total_order_amount = 0
    for item in items:
        total += item.total

    context={'order': order,
             'order_items': order_items,
             'items': items,
             'total': total,
             }
    return render(request, 'admin/view_order.html', context)
