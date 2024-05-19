from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from app.models import *

def deletemanageorder(request):
    id = request.GET.get('id', '')  # lấy id khi người dùng vlick vào sản phẩm nào đó
    order = get_object_or_404(Order, id=id)
    print(order)
    items = OrderItem.objects.filter(order=order)
    print(items)
    if request.method == 'POST':
        items.delete()
        order.delete()
        messages.success(request, 'Xóa đơn hàng thành công')
        return redirect('manageorder')
    context = {'order': order}

    return render(request, 'admin/deletemanageorder.html', context)