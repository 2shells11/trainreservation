from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.template import Template, Context
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from res.models import Passenger
from django.template import Context

d = {"AC1": 10, "AC2": 20, "AC3": 5}

# Create your views here.
def HomePage(request):
    ll=[]
    if request.method == 'POST':
   # d = {"AC1": 10, "AC2": 10, "AC3": 10}
    #available_seats = 0
        print("ghjghjgh")

    if request.method == "POST":
        category = request.POST.get('category')
        print(d[category])
        print("ghjghjhjhfhjkj")
        Passengers = int(request.POST.get('Passengers'))
        print(type(Passengers))
        if d[category] > Passengers:
            available_seats = d[category]
            print("inside")
            d[category] = d[category] - Passengers
            print(d[category])
            messages.success(request, "Tickets Booked successfully in")
            ll.append(category)
            print(ll)


        else:
            available_seats = list(filter(lambda e: e[1] > Passengers, d.items()))
            for i in range(len(available_seats)):
                ll.append(available_seats[i][0])
                print("Seats available in :", available_seats[i][0])
            #context = {'m': ll}
            messages.success(request, "Seats available in")

        passenger = Passenger(category=category, Passengers=Passengers)
        passenger.save()
        print(ll)
    # if d[category] > Passengers:
    #     available_seats = d[category]
    #     d[category] = d[category] - Passengers
     #   return redirect('proceed')
    context = {"Available_seats": ll}
    return render(request, 'home.html', context)




def ProceedPage(request):
    # if request.method == 'POST':
    #     c = request.GET.get('category')
    #     p = request.GET.get('Passengers')
    #     print(c)
    #     if d['c'] > p:
    #         available_seats = d['c']
    #         d['c'] = d['c'] - p
    #     else:
    #         available_seats = dict(filter(lambda e: e[c] > p, d.items()))
    #     #context = {"Available_seats": available_seats}
    return render(request, 'proceed.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')