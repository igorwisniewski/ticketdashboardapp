from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .form import RegisterCustomerForm

# register a customer
def register_customer(request):
    if request.method =='POST':
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)  
            var.is_customer = True
            var.save()
            messages.success(request, 'You acmoplished creating account, congratulations!')
            return redirect('login')
        else: 
            messages.warning(request, 'Something went wrong, Please check form details')
            return redirect('register-customer')
    else:
        form = RegisterCustomerForm()
        context = {'form':form}
        return render(request, 'users/register-customer.html', context)

#Login user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, 'Login successfull!')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong, Please check form details')
            return redirect('login')
    else:
        return render(request, 'users/login.html')
    
#logout
def logout_user(request):
    logout(request)
    messages.success(request, 'Logout successfull!')
    return redirect('login')
    