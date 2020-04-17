from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<em>My second app </em>")

def help(request):
    data = {'add_me':"Help page"}
    return render(request,'AppTwo/index.html',context=data)
