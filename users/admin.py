from django.contrib import admin

# Register your models here.

from .models import User, profile

class UserAdmin(admin.ModelAdmin):
    list_display=("id", "first_name", "last_name", "email")

admin.site.register(User, UserAdmin)
admin.site.register(profile)