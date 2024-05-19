from django.contrib import messages
from django.shortcuts import render
from app.models import *



def myOrder(request):
    slide_hidden = "hidden"
    fixed_height = "20px"
    show_manage = 'show'  # Đảm bảo rằng biến show_manage đã được khai báo
    user_not_login = 'none'

    my_orders = Order.objects.filter(customer=request.user)
    order_items = {}  # Tạo một từ điển để lưu trữ các đơn hàng và mặt hàng tương ứng
    order_addresses = {}  # Tạo một từ điển để lưu trữ đơn hàng và thông tin địa chỉ tương ứng
    order_total_amounts = {}

    for order in my_orders:
        items = OrderItem.objects.filter(order=order)
        order_items[order] = items
        total_order_amount = 0
        for item in items:
            total_order_amount += item.total
            print("tong gia order : ")
            print(total_order_amount)
        order_total_amounts[order.id] = total_order_amount

        address = order.address  # Truy cập vào đối tượng Address liên kết với đơn hàng
        order_addresses[order] = address
        if order.id in order_total_amounts:  # Sửa lại kiểm tra xem order.id có trong order_total_amounts
            print(f"Giá trị đã được lưu cho đơn hàng '{order}': {order_total_amounts[order.id]}")
        else:
            print(f"Không tìm thấy giá trị cho đơn hàng '{order}' trong order_total_amounts.")

    order_total_amounts_list = [(order_id, total_amount) for order_id, total_amount in order_total_amounts.items()]  # Đặt danh sách ngoài vòng lặp

    context = {
        'user_not_login': user_not_login,
        'order_addresses': order_addresses,
        'order_items': order_items,
        'slide_hidden': slide_hidden,
        'fixed_height': fixed_height,
        'show_manage': show_manage,
        'my_order': my_orders,
        'order_total_amounts': order_total_amounts,
        'order_total_amounts_list': order_total_amounts_list,  # Đưa vào context
    }
    return render(request, 'app/my_order.html', context)





