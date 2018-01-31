from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import Group

from .models import User
from .forms import UserCreationForm


class UserAdmin(DjangoUserAdmin):
    list_display = ['email', 'full_name', 'last_login']
    list_filter = ['is_active', 'is_admin']
    search_fields = ['email']
    fieldsets = None
    add_form = UserCreationForm

    readonly_fields = ['last_login']
    ordering = ['email']

    def get_fieldsets(self, request, obj=None):
        return super(DjangoUserAdmin, self).get_fieldsets(request, obj)


UserAdmin.add_fieldsets = UserAdmin.fieldsets

admin.site.register(User, UserAdmin)

admin.site.unregister(Group)
