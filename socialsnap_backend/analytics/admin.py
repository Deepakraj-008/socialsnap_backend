from django.contrib import admin
from .models import AnalyticEvent

@admin.register(AnalyticEvent)
class AnalyticEventAdmin(admin.ModelAdmin):
    list_display = ("user", "event_type", "created_at")
    search_fields = ("event_type", "user__username")
    list_filter = ("event_type", "created_at")

