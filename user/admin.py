from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser, Grade, Institution

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('phone', 'middle_name', 'grade', 'institution')}),
    )

admin.site.register(CustomUser, MyUserAdmin)
admin.site.register(Grade)
admin.site.register(Institution)