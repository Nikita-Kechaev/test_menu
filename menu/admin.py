from django.contrib import admin

from .models import Menu


@admin.register(Menu)
class Menu_admin(admin.ModelAdmin):
    list_display = [
        "label",
    ]
