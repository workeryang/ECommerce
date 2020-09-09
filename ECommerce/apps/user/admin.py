from django.contrib import admin

# Register your models here.
from ECommerce.apps.user.models import UserInfo, Role

admin.site.register(UserInfo)
admin.site.register(Role)
