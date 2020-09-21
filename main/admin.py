from django.contrib import admin
from .models import GuestResponse


@admin.register(GuestResponse)
class GuestResponseAdmin(admin.ModelAdmin):
    pass