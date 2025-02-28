from django.contrib import admin

from main.models import ShortedURL


@admin.register(ShortedURL)
class ShortedURLAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'shorted_url', 'clicks')