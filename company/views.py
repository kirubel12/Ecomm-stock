from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import PostForm

# Create your views here.


def Home(request):
    return render(request, 'company/index.html')


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
                return redirect('login-comp')
        else:
            return redirect('register')
    return render(request, 'company/register.html')


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


def Dashboard(request):
    return render(request, 'company/dashboard.html')


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

