from django.http import HttpResponseRedirect,HttpResponse  
from django.template.loader import get_template
from django.template import Template,Context

from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.


def dashboard(request):
    return HttpResponse("Admin Hello world")
