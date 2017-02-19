from django.http import HttpResponseRedirect,HttpResponse  
from django.template.loader import get_template
from django.template import Template,Context

from django.shortcuts import get_object_or_404, render, redirect



from basic.user import *
from basic.admin import *
from basic.food import *
from basic.booking import *
from basic.guestHouse import *
from basic.dataBase import *


# Create your views here.


def dashboard(request):
	if type=='admin':
		visitor=get_object_or_404(Administrator, Id=request.session['visitor']['id'])
	else:
		visitor=get_object_or_404(User, Id=request.session['visitor']['id'])
	return render(request, 'user/profile.html',{'visitor':visitor})
    # return HttpResponse("User Hello world")
