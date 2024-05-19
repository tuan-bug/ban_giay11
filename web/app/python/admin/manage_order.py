from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from app.models import *

def manageorder(request):
    orders = Order.objects.all()

    context = {'orders': orders}
    return render(request, 'admin/manageorder.html', context)



