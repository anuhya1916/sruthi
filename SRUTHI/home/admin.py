from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Requests,Event_Head,events_interested

# Register your models here.


class MyAdminSite(AdminSite):
    site_header = 'SRUTHI administration'

admin_site = MyAdminSite(name='myadmin')
admin.site.register(Requests)
admin.site.register(Event_Head)
admin.site.register(events_interested)
#admin_site.register(MyModel)


