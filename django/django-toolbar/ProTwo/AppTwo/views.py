from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.

def index(request):
    return HttpResponse("<em>My second app </em>")

def help(request):
    data = {'add_me':"Help page"}
    return render(request,'AppTwo/index.html',context=data)

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request,'AppTwo/users.html',context=user_dict)
