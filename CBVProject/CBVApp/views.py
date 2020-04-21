from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView
from CBVApp.models import School, Student


class IndexView(TemplateView):
    template_name = "CBVApp/index.html"


class SchoolListView(ListView):
    model = School
    context_object_name = 'schools'


class SchoolDetailView(DetailView):
    model = School
    context_object_name = 'school_detail'
