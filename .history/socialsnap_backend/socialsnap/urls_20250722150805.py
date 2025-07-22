from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

def home_view(request):
    return HttpResponse("<h1>Welcome to SocialSnap API Server</h1>")

urlpatterns = [
    path("", home_view),  # <-- this line adds the root path
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),
    path("api/posts/", include("posts.urls")),
    path("api/chat_messages/", include("chat_messages.urls")),
    path("api/ai/", include("ai.urls")),
    path("api/analytics/", include("analytics.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
