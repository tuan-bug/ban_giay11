from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from app.models import *


def manageProduct(request):
    products = Product.objects.all()
    form = AddProduct()
    context = {'products': products}
    return render(request, 'admin/managementProduct.html', context)


def addProduct(request):
    if request.method == 'POST':
        images = request.FILES.getlist('listImages')
        product_form = AddProduct(request.POST, request.FILES)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.save()  # Lưu đối tượng Product trước
            product_form.save_m2m()  # Lưu các trường ManyToMany

            # Lưu các hình ảnh liên quan
            for image in request.FILES.getlist('images'):
                product.image.create(image=image)

            for image in images:
                ImagesProduct.objects.create(product=product, image=image)

            # Lưu các kích cỡ và số lượng liên quan
            sizes = request.POST.getlist('sizes[]')
            quantities = request.POST.getlist('quantities[]')
            for size, quantity in zip(sizes, quantities):
                if size and quantity:
                    Size.objects.create(product=product, size=size, quantity=quantity)

            messages.success(request, 'Thêm sản phẩm thành công')
            return redirect('manageProduct')
    else:
        product_form = AddProduct()
    return render(request, 'admin/addProduct.html', {'product_form': product_form})


def editProduct(request):
    product_id = request.GET.get('id', '')
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        images = request.FILES.getlist('listImages')
        product_form = AddProduct(request.POST, request.FILES, instance=product)

        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.save()  # Lưu đối tượng Product trước
            product_form.save_m2m()  # Lưu các trường ManyToMany
            for image in request.FILES.getlist('images'):
                product.image.create(image=image)

            for image in images:
                ImagesProduct.objects.create(product=product, image=image)

            # Xóa các kích cỡ cũ và lưu các kích cỡ và số lượng mới
            Size.objects.filter(product=product).delete()
            sizes = request.POST.getlist('sizes[]')
            quantities = request.POST.getlist('quantities[]')
            for size, quantity in zip(sizes, quantities):
                if size and quantity:
                    Size.objects.create(product=product, size=size, quantity=quantity)

            messages.success(request, 'Chỉnh sửa sản phẩm thành công')
            return redirect('manageProduct')
    else:
        product_form = AddProduct(instance=product)
        sizes_and_quantities = product.sizes.all()  # Sử dụng related_name 'sizes'

    return render(request, 'admin/editProduct.html', {
        'product_form': product_form,
        'product': product,
        'sizes_and_quantities': sizes_and_quantities,
    })


def deleteProduct(request):
    id = request.GET.get('id', '')  # lấy id khi người dùng vlick vào sản phẩm nào đó
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Category deleted successfully!')
        return redirect('manageProduct')
    context ={'product': product}
    return render(request, 'admin/deleteProduct.html', context)

def viewProduct(request):
    id = request.GET.get('id', '')  # lấy id khi người dùng vlick vào sản phẩm nào đó
    user = request.user
    print(user)
    product = get_object_or_404(Product, id=id)
    sizes = Size.objects.filter(product=product)
    context = {'product': product,
               'sizes': sizes,
               }
    return render(request, 'admin/view_product.html', context)