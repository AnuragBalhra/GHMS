from django.conf.urls import include,url


from basic.administrator.views import *

urlpatterns = [
    url(r'^$',dashboard, name='dashboard'),
    url(r'^search/$',search, name='search'),
    url(r'^showBooking/$',showBooking, name='showBooking'),
    url(r'^showUser/$',showUser, name='showUser'),
    url(r'^delUser/$',delUser, name='delUser'),
    url(r'^showRoom/$',showRoom, name='showRoom'),
    url(r'^delRoom/$',delRoom, name='delRoom'),
    url(r'^showRooms/$',showRooms, name='showRooms'),
    url(r'^cancel/$',cancel, name='cancel'),
    url(r'^confirm/$',confirm, name='confirm'),
    url(r'^addObj/$',addObj, name='addObj'),
    # url(r'^profile/$',profile , name='profile'),
    # url(r'^search/$',search , name='search'),
    # url(r'^bookings/$',bookings , name='bookings'),

]