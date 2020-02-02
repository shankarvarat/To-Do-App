from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .form import TodoForm
from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from datetime import datetime



# Create your views here.
def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth.login(request,user)
                return redirect('/index')
            else:

                return HttpResponse("Your account was inactive.")
        else:
            return HttpResponse("Invalid login details given")

    else:
                return render(request,'login.html')

@login_required
def logoutuser(request):
            logout(request)
            return redirect("/index")
def signupform(request):
    if request.method=="POST":
        formdata=UserCreationForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            return render(request,"home.html")
        else:
            m="Invalid Form"
            return render("signup.html",{"form":formdata,"m":m})
    else:
        form=UserCreationForm()
        print(form)

        return render(request,"signup.html",{"form": form})
@login_required
def home(request):
    if User.is_active:
        #user=request.User
        name=request.user

        data=works.objects.all()
        com=works.objects.filter(status="Completed",user=name)
        Not=works.objects.filter(status="Not Started",user=name)
        pro=works.objects.filter(status="Work in Progress",user=name)
        print("user is active")

        return render(request,'home.html',{'data':data,'com':com,'Not':Not,'pro':pro,"name":name})
    else:
        print("user is not active")
        return render(request,"login.html")

@login_required
def create(request):
    try:
        if request.method=='POST':
            form=TodoForm(request.POST)

            print("form",form)


            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.created_date=datetime.now()
                print(">>>",post)
                post.save()
                print(post,"shdbzkvhb")
                return redirect('/home')
            else:
                return render(request, 'home.html', {'form': form})
        else:
            form = TodoForm()
            # print(">>>>",form)
            return render(request, 'create.html', {'form': form})
    except Exception as e: 
                 return render(request, 'create.html', {'form': form})





