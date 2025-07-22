from django.contrib import admin
from django.utils import timezone
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("sender", "recipient", "content", "created_at", "is_disappearing")
    search_fields = ("content", "sender__username", "recipient__username")
    list_filter = ("is_disappearing", "created_at")
    actions = ["delete_expired"]

    def delete_expired(self, request, queryset):
        expired = queryset.filter(is_disappearing=True, expires_at__lt=timezone.now())
        expired.delete()
    delete_expired.short_description = "Delete expired messages"

