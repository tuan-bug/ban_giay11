from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import *

@login_required
def editInformation(request):
    user = request.user
    if request.method == 'POST':

        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        return redirect('information')
    
    form = CreateUserForm(instance=user, 
                       initial={
                                'last_name': user.last_name, 
                                'first_name': user.first_name,
                                'email': user.email,
                                })

    context = {'form': form}
    return render(request, 'app/edit_information.html', context)
