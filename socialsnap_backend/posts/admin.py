from django.contrib import admin
from django.utils import timezone
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("user", "caption", "created_at", "is_story")
    search_fields = ("caption", "user__username")
    list_filter = ("is_story", "created_at")
    actions = ["delete_expired_stories"]

    def delete_expired_stories(self, request, queryset):
        expired = queryset.filter(is_story=True, expires_at__lt=timezone.now())
        expired.delete()
    delete_expired_stories.short_description = "Delete expired stories"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "content", "created_at")
    search_fields = ("content", "user__username")

