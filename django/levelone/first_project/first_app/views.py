from django.shortcuts import render
from django.http import HttpResponse  #importing httpresponse object

# Create your views here.
#each views in this app has its individual function
#each view takes one prameter
#each view must return httpresponse object

def index(request):  #request param can be of any name
    #return HttpResponse("hello world!") #we can html code also
    my_dict = {'insert_me':"hello i am from views.py"}
    #return render(request,'first_app/index.html',context=my_dict)
    return render(request,'index.html',context=my_dict) #this ts to show staticfiles image
