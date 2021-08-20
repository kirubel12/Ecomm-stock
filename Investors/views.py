from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

from company.models import PostModel
from .decorators import allowed_users, unauthorized_user
from .forms import CompUserRegistor


def Home(request):
    return render(request, 'investor/index.html')


@unauthorized_user
def Register(request):
    form = CompUserRegistor()
    if request.method == 'POST':
        form = CompUserRegistor(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='investor')
            user.groups.add(group)
            return redirect('login')
    context = {'form': form}
    return render(request, 'investor/register.html',context)

@unauthorized_user
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


@allowed_users(allowed_roles='investor')
def Dashboard(request):
    return render(request, 'investor/dashboard.html')


@allowed_users(allowed_roles='investor')
def Buystock(request):
    Stocks = PostModel.objects.all()
    context = {'stocks':Stocks}
    return render(request, 'investor/buy_stock.html', context)


def Logoutuser(request):
    logout(request)
    return redirect('home')
