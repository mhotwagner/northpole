from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import OrnamentDevice


@admin.register(OrnamentDevice)
class OrnamentAdmin(admin.ModelAdmin):
    fields = ('mac_address', 'nickname')

