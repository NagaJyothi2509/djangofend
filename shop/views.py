from django.shortcuts import render, HttpResponse, redirect
# from .models import Product, Photo, order
from django.contrib.auth. models import User
from django.contrib import messages
import requests
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from .models import shop_user




def index(request):
    return render(request, "shop/Admin_login.html")

def connect(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            messages.info(request,"Invalid Username or Password")
            return redirect('/')
    return HttpResponse("Something is wrong")

def solve(request):
    response=requests.get('https://api.covid19api.com/countries').json()
    return render(request,'shop/new.html',{'response':response})

def dashboard(request):
    user=shop_user.objects.all()
    context={
        'Total_admin':len(user)
    }
    return render(request,"shop/dashboard.html",context)

def handellogout(request):
    logout(request)
    return redirect('/dashboard')




def handelsignup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        user = User.objects.all()
        count = 0
        for i in user:
            if i.username == username:
                count += 1
        if count == 0:
            if len(username) != 0 and len(firstname) != 0 and len(lastname) != 0:
                if pass1 == pass2 and len(pass1) != 0:
                    myuser = User.objects.create_user(username, email, pass1)
                    myuser.first_name = firstname
                    myuser.last_name = lastname
                    myuser.save()
                    return HttpResponse("Your account has been successfully created--")
                else:
                    return HttpResponse("password && confarm password is not same--")
            else:
                return HttpResponse("please filled the the blanks before submit--")
        else:
            return HttpResponse("username is already exit--")

    else:
        return HttpResponse("404 page not found")

def handellogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("unsuceessfull login")
    else:
        return HttpResponse("404 page not found")


@csrf_exempt
def my_view(request):
    return HttpResponse('Hello world')
def userinfo(request):
    userlist=User.objects.all()
    #response=requests.get('https://api.covid19api.com/countries').json()
    return render(request,'shop/new2.html',
                  {'userlist':userlist})

def dashboard(request):
    return render(request,'shop/new3.html')

def managereviews(request):
    return render(request,'shop/new4.html')

def manageproperties(request):
    return render(request,'shop/new5.html')

def managerental(request):
    return render(request,'shop/new6.html')


