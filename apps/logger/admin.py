from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Log


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('created', 'ornament', 'message')
    fields = (('ornament',),
              ('message',),)

