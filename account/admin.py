from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

@admin.register(User)
class MyUserAdmin(UserAdmin):
    # This allows you to see the username and email in the list view
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    raw_id_fields = ['user']