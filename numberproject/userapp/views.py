from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['Username']
        first_name = request.POST['First_name']
        last_name = request.POST['Last_name']
        email = request.POST['email']
        password = request.POST['new-password']
        confirm_password = request.POST['confirm password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,first_name=first_name, last_name=last_name,password=password,email=email)
                user.save();
                return redirect('login')
            print("user created")
        else:
            messages.info(request,'password not matched')
            return redirect('register')
        return redirect('/')  # homepage
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')