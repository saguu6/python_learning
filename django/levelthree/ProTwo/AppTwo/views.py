from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.froms import NewUserForm
# Create your views here.

def index(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request,'AppTwo/index.html',context=user_dict)
    # return render(request,'AppTwo/index.html')


def help(request):
    data = {'add_me':"Help page"}
    return render(request,'AppTwo/index.html',context=data)

def users(request):

    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("error form invalid")

    return render(request,'AppTwo/users.html',{'form':form})
