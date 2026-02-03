
# Register your models here.
from django.contrib import admin
from .models import Account
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ['id','name','mobile','email','address']


admin.site.register(Account,AccountAdmin)