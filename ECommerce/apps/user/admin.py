from django.contrib import admin

# Register your models here.
from ECommerce.apps.user.models import Order

admin.site.register(Order)
