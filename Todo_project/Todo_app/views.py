from django.shortcuts import render,redirect
from .models import *
from .form import TodoForm

# Create your views here.
def home(request):
    data=todo.objects.all
    com=todo.objects.filter(status="Completed")
    Not=todo.objects.filter(status="Not Started")
    pro=todo.objects.filter(status="Work in Progress")


    return render(request,'index.html',{'data':data,'com':com,'Not':Not,'pro':pro})
def create(request):
    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            form=TodoForm()
            return redirect('/home')
        else:
            return render(request, 'create.html', {'form': form})

    else:
        form = TodoForm()

        return render(request, 'create.html', {'form': form})





