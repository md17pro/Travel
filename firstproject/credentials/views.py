from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def reg(request):
    if request.method=='POST':
        username =request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email= request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if cpassword==password:
            if  User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('Register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect('Register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password,email=email)
                user.save();
                print("user created")
                return redirect('login')
        else:
            messages.info(request,'Password Not matching')
            return redirect('Register')
        return redirect('/')
    return render(request,'register.html')

def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
    else:
        messages.info(request,"Invalid Credentials")
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')