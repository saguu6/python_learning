from django.shortcuts import render
from firstapp.models import Topic,Webpage,AccessRecord

# Create your views here.
def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    my_dict = {'access_records':webpage_list}
    return render(request,'firstapp/index.html',context=my_dict)
