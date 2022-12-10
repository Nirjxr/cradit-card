from django.contrib import admin
from login.models import UserInfo

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=('email','password')
    
admin.site.register(UserInfo,UserAdmin)




