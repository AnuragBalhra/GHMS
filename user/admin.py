from django.contrib import admin
from .models import Admin,User,Food,Room,Booking


class PersonAdmin(admin.ModelAdmin):
	list_display=('Id', 'Name', 'Password', 'Email')
	search_fields=('Id', 'Name', 'Password', 'Email')

class FoodAdmin(admin.ModelAdmin):
	list_display=('Id', 'Name', 'Status')
	search_fields=('Id', 'Name', 'Status')


class RoomAdmin(admin.ModelAdmin):
	list_display=('Id', 'Cost', 'Status')
	search_fields=('Id', 'Cost', 'Status')


class BookingAdmin(admin.ModelAdmin):
	list_display=('GNR', 'UserId', 'RoomId','FoodId', 'StartTime', 'EndTime', 'AmountReq', 'AmountPaid', 'Status', 'Reason', 'BookingTime')
	search_fields=('GNR', 'UserId', 'RoomId','FoodId', 'StartTime', 'EndTime', 'AmountReq', 'AmountPaid', 'Status', 'Reason', 'BookingTime')
	list_filter=('StartTime', 'EndTime', 'BookingTime')


admin.site.register(Admin, PersonAdmin)
admin.site.register(User, PersonAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Booking, BookingAdmin)


