"""GHMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin


from GHMS.views import *

urlpatterns = [
    url(r'^Admin/', admin.site.urls),
    url(r'^hello/$', hello),
    url(r'^admin/',include('basic.administrator.urls'),name='admin'),
    url(r'^user/',include('basic.user.urls'),name='user'),
    url(r'^$',home),
    url(r'^login/$',login , name='login'),
    url(r'^logout/$',logout , name='logout'),
    # url(r'^profile/$',profile , name='profile'),
    # url(r'^search/$',search , name='search'),
    # url(r'^bookings/$',bookings , name='bookings'),

]