from django.shortcuts import render
from . import forms
#or we can use from basicapp import forms
# Create your views here.

def index(request):
    return render(request,'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("validation is complete")
            print("NAme :"+form.cleaned_data['name'])
            print("email :"+form.cleaned_data['email'])
            print("text :"+form.cleaned_data['text'])
    return render(request,'basicapp/forms.html',{'form':form})
