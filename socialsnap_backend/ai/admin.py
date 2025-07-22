from django.contrib import admin
from .models import AIInteraction

@admin.register(AIInteraction)
class AIInteractionAdmin(admin.ModelAdmin):
    list_display = ("user", "input_text", "response", "created_at")
    search_fields = ("input_text", "response", "user__username")

