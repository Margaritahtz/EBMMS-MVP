from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import utils
from math import remainder
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template import RequestContext



def home(request):
    time = utils.timer_save()
    
    return render(request, 'base/home.html')


def loginpage(request):
    return render(request, 'base/login.html')

def temp(request):
    return render(request, 'base/temp.html')


def humidity(request):
    return render(request, 'base/humdt.html')

def accl(request):
    return render(request, 'base/accl.html')


def stress(request):
    return render(request, 'base/stress.html')

def err(request):
    return render(request, 'base/404.html')

def rainfall(request):
    return render(request, 'base/rainfall.html')

def index(request):
    #  if request.method == "POST":
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     User = authenticate(request, username=username, password=password)

    #     if User is not None:
    #      login(request, User)
    #      return redirect('index')
    #     else:
        
    #         redirect('login')

    
    #  else:
        return render(request, 'base/index.html', {})


