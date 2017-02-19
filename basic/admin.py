from django.contrib import admin
# Register your models here.

from basic.administrator.administrator import Administrator
class PersonAdmin(admin.ModelAdmin):
	list_display=('Id', 'Name', 'Password', 'Email')
	search_fields=('Id', 'Name', 'Password', 'Email')
admin.site.register(Administrator, PersonAdmin)


from .booking import Booking
class BookingAdmin(admin.ModelAdmin):
	list_display=('GNR', 'UserId', 'RoomId','FoodId', 'StartTime', 'EndTime', 'AmountReq', 'AmountPaid', 'Status', 'Reason', 'BookingTime')
	search_fields=('GNR', 'UserId', 'RoomId','FoodId', 'StartTime', 'EndTime', 'AmountReq', 'AmountPaid', 'Status', 'Reason', 'BookingTime')
	list_filter=('StartTime', 'EndTime', 'BookingTime')
admin.site.register(Booking, BookingAdmin)


from .food import Food
class FoodAdmin(admin.ModelAdmin):
	list_display=('Id', 'Name', 'Status')
	search_fields=('Id', 'Name', 'Status')
admin.site.register(Food, FoodAdmin)


from .room import Room
class RoomAdmin(admin.ModelAdmin):
	list_display=('Id', 'Cost', 'type')
	search_fields=('Id', 'Cost', 'type')
admin.site.register(Room, RoomAdmin)


from .user.user import User
class PersonAdmin(admin.ModelAdmin):
	list_display=('Id', 'Name', 'Password', 'Email')
	search_fields=('Id', 'Name', 'Password', 'Email')
admin.site.register(User, PersonAdmin)
