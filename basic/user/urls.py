from django.conf.urls import include,url


from basic.user.views import *

urlpatterns = [
    url(r'^$',dashboard, name='dashboard'),
    url(r'^search/$',search, name='search'),
    url(r'^showBooking/$',showBooking, name='showBooking'),
    # url(r'^profile/$',profile , name='profile'),
    # url(r'^search/$',search , name='search'),
    # url(r'^bookings/$',bookings , name='bookings'),

]