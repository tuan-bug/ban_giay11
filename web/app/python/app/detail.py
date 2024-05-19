from django.shortcuts import get_object_or_404, render
from app.models import Cart
from app.models import *


def detail(request):
    slide_hidden = "hidden"
    fixed_height = "20px"
    fixed_comment = "100px"
    #check xem phải admin không
    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'
    total_all = 0
    count = 0
    if request.user.is_authenticated:
        customer = request.user
        items = Cart.objects.filter(user=customer)
        for item in items:
            print(item) 
        user_not_login = "none"
        user_login = "show"
        for item in items:
            print(item)
            item.total = item.product.price * item.quantity
            total_all += item.product.price * item.quantity
            count += item.quantity
    else:
        items = []
        user_not_login = "show"
        user_login = "none"
    id = request.GET.get('id', '') # lấy id khi người dùng Click vào sản phẩm nào đó
    user = request.user
    products = get_object_or_404(Product, id=id)

    products.formatted_price = "{:,.0f}".format(products.price)
    lstImage = ImagesProduct.objects.filter(product=products)
    lstSize = Size.objects.filter(product=products)
    for item in lstImage:
        print(item.ImageURL)
    categories = Category.objects.filter(is_sub=False)  # lay cac damh muc lon
    context = {
               'products': products,
               'items': items,
               'total_all': total_all,
               'count': count,
               'user_login': user_login,
               'user_not_login': user_not_login,
               'categories': categories,
               'slide_hidden': slide_hidden,
               'fixed_height': fixed_height,
               'fixed_comment': fixed_comment,
               'show_manage': show_manage,
               'lstImage': lstImage,
               'lstSize': lstSize,
               }
    return render(request, 'app/detail.html', context)
