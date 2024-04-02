from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'phone')
    list_display_links = ('username',)

admin.site.register(User, UserAdmin)

