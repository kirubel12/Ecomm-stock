from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from company.models import PostModel

def Home(request):
    return render(request, 'investor/index.html')


def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("Username already taken")
            elif User.objects.filter(email=email):
                print("Email already taken")
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password1)
                user.save()
                return redirect('login')
        else:
            return redirect('register')
    return render(request, 'investor/register.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login')

    return render(request, 'investor/login.html')


def Dashboard(request):
    return render(request, 'investor/dashboard.html')


def Buystock(request):
    Stocks = PostModel.objects.all()
    context = {'stocks':Stocks}
    return render(request, 'investor/buy_stock.html', context)


def Logoutuser(request):
    logout(request)
    return redirect('home')
