from django.contrib import admin
from login.models import Registaration

# Register your models here.

class AdminRegistration(admin.ModelAdmin):
    list_display=['fname','lname','age','number','alt_number','email','country','password']
    
admin.site.register(Registaration,AdminRegistration)