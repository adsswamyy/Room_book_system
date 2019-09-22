from django.contrib import admin
from roomapp.models import accounts
# Register your models here.
class accounts_admin(admin.ModelAdmin):
    list_display = ['email','username','Date_Joiend','last_login','password','confiem_password']
admin.site.register(accounts,accounts_admin)
