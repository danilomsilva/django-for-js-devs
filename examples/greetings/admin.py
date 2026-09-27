from django.contrib import admin

from .models import Greeting, GreetingCategory


@admin.register(Greeting)
class GreetingAdmin(admin.ModelAdmin):
    list_display = ["message", "category", "created_at"]
    list_filter = ["category"]


@admin.register(GreetingCategory)
class GreetingCategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
