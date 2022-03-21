import imp
import re
from turtle import update
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import MenuItem, Order, Review, UserExt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def register(request):
    print(request)
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("auto:home"))
    if request.method == "POST":
        user = User.objects.create_user(username = request.POST["usern"], email = request.POST["email"], password= request.POST["passw"])
        user.save()


        userEx = UserExt(user = user, roll = int(request.POST["roll"]), phone = int(request.POST["phone"]), isStaff = True if request.POST["isStaff"] == "True" else False)
        userEx.save()

        login(request, user)
        return HttpResponseRedirect(reverse("auto:home"))
    return render(request, 'home/registration.html')

def login_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("auto:home"))
    if request.method =="POST":
        
        username = request.POST['username']
        password = request.POST['password']
        #print(username,' ',password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("auto:home"))
        else:
            return HttpResponse("Ex occured")

    return render(request, 'home/login.html')

def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("auto:login"))

def home(request):
    context = {"username" : request.user.username}
    return render(request, 'home/home.html', context)

def profile(request):
    context = {
        'ext' : UserExt.objects.get(user = request.user)
        }
    return render(request, 'home/profile.html', context)

def menu(request, hall):
    items = MenuItem.objects.filter(hall = hall)

    rat = []

    for item in items:
        avg = {'rating' : 0}
        it = Review.objects.filter(item = item)
        for i in it:
            avg['rating'] += i.rating
        avg['rating'] = (avg['rating']/len(it)) if len(it) > 0 else 0
        rat.append(avg)

    context = {
        'items':items,
        'ratings': rat
        }
    return render(request, 'home/menu.html', context)

def orders(request):
    ords = Order.objects.filter(user = UserExt.objects.get(user = request.user)).exclude(paystatus = 0).order_by('-id')    
    tot = 0
    for i in ords:
        t = i.item.price* i.quantity
        if i.paystatus == '2':
            tot+= t

    context = {
        'orders' : ords,
        'total' : tot,
    }
    return render(request, 'home/orders.html', context)

def tocart(request,hall, itemId):
    item = MenuItem.objects.get(id=int(itemId))
    order = Order(hall = hall, item = item, quantity = 1, dt = 0, paymode = 0, paystatus=0, user = UserExt.objects.get(user = request.user))
    order.save()
    return HttpResponseRedirect(reverse('auto:cart'))

def savecart(request, orderId):
    if request.method == "POST":
        order = Order.objects.get(id = orderId)
        if int(request.POST['quant']) <= 0:
            order.delete()
        else:
            order.quantity = int(request.POST['quant'])
            order.save()

    return HttpResponseRedirect(reverse('auto:cart'))

def cart(request):
    ords = Order.objects.filter(user = UserExt.objects.get(user = request.user), paystatus = 0)
    lis = []
    tot = 0
    for i in ords:
        di = {}
        t = i.item.price* i.quantity
        di['name'] = i.item.item
        di['cost'] = t
        tot+= t
        lis.append(di)

    context = {
        'orders' : ords,
        'costs' : lis,
        'total' : tot,
    }
    return render(request, 'home/cart.html', context)

def paycart(request, paystat):
    ords = Order.objects.filter(user = UserExt.objects.get(user = request.user), paystatus = 0)
    
    for i in ords:
        if int(paystat) == 1:
            i.paystatus = 1
        elif int(paystat) == 2:
            i.paystatus = 2
        else:
            i.paystatus = 0
        i.save()

    return HttpResponseRedirect(reverse('auto:orders'))

def contact_us(request):
    return render(request, 'home/contact_us.html')