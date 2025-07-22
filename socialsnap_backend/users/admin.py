from django.contrib import admin
from .models import User, Streak

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_premium", "snap_score", "last_active")
    search_fields = ("username", "email")
    list_filter = ("is_premium",)
    actions = ["make_premium"]

    def make_premium(self, request, queryset):
        queryset.update(is_premium=True)
    make_premium.short_description = "Mark selected users as premium"

@admin.register(Streak)
class StreakAdmin(admin.ModelAdmin):
    list_display = ("user", "friend", "count", "last_interaction")
    search_fields = ("user__username", "friend__username")

