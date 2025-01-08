from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff',
                    'telegram_chat_id')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('telegram_chat_id',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('telegram_chat_id',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
