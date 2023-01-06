from django.contrib import admin
from api.models import CustomUser, Player
from api.custom_user import CustomUserAdmin

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Player)