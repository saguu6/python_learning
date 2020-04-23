from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.http import HttpResponse
from . import models
from django.core.urlresolvers import reverse_lazy
# Create your views here.
# def index(request):
#     return render(request,'index.html')

# class CBView(View):
#     def get(self,request):
#         return HttpResponse("CLASS BASED VIEWS")


class IndexView(TemplateView):
    template_name = 'index.html'  #'basic_app/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'basic injection'
        return context

class SchoolListView(ListView):
    context_object_name = "schools" #optional to name the context
    model = models.School
    #return school_list context

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    #return school
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
