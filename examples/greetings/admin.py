from django.contrib import admin

from .models import Greeting


@admin.register(Greeting)
class GreetingAdmin(admin.ModelAdmin):
    list_display = ["message", "created_at"]
