from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import PostForm, UserRegister
from .decorators import unauthorized_user, allowed_users
from django.contrib.auth.models import Group

from .models import PostModel


def Home(request):
    return render(request, 'company/index.html')


@unauthorized_user
def Register(request):
    form = UserRegister()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='startup')
            user.groups.add(group)
            return redirect('login-comp')
    context = {'form': form}
    return render(request, 'company/register.html', context)


@unauthorized_user
def LoginCompany(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user)
            return redirect('dashboard-comp')
        else:
            return redirect('login-comp')

    return render(request, 'company/login.html')


@allowed_users(allowed_roles='startup')
def Dashboard(request):
    stock = PostModel.objects.all()
    context = {'stocks':stock}
    return render(request, 'company/dashboard.html',context)


@allowed_users(allowed_roles='startup')
def Post(request):

    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            print("saved successfully")
            return redirect('comp-home')
        else:
            print("error" , form.errors)
    context = {'form':form}
    return render(request, 'company/post.html',context )


def LogoutComp(request):
    logout(request)
    return redirect('comp-home')


def UpdateStock(request, stock_id):
    Stock = PostModel.objects.get(pk=stock_id)
    form = PostForm(request.POST or None, request.FILES or None, instance=Stock)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            print("saved successfully")
            return redirect('dashboard-comp')
        else:
            print("error" , form.errors)
    context = {'Stock':Stock,'form':form}
    return render(request, 'company/update_stock.html',context)