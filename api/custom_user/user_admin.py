from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .user_forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email', 'id', 'is_admin')
    list_filter = ()
    fieldsets = (
        ('Login', {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'surname')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_admin', 'is_superuser', 'groups', 'user_permissions',)}),
        ('Important dates', {"fields": ("last_login",)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'surname', 'username', 'email', 'password1', 'password2'),
        }),
    )
    # search_fields = ('username',)
    search_fields = ('username', 'email')
    ordering = ('username',)
