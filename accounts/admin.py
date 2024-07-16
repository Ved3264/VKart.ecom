from django.contrib import admin
from . models import Account
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
      list_display=('username','email','first_name','last_name','last_login','date_joined','is_active')
      list_display_links=('username','email')
      readonly_fields=('last_login','date_joined')
      ordering=('-date_joined',)

      filter_horizontal=()
      list_filter=()
      fieldsets=()

# Register your models here.
admin.site.register(Account,AccountAdmin)