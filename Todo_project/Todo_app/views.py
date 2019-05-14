from django.shortcuts import render
from .models import *
from .form import TodoForm

# Create your views here.
def home(request):
    data=todo.objects.all
    form=TodoForm()
    return render(request,'index.html',{'form':form,'data':data})