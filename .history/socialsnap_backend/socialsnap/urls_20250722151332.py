# socialsnap/urls.py
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

def home_view(request):
    return HttpResponse("<h1>Welcome to SocialSnap API Server</h1>")

urlpatterns = [
    path("", home_view),
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),           # Users endpoints
    path("api/posts/", include("posts.urls")),           # Posts endpoints
    path("api/chat_messages/", include("chat_messages.urls")), # Chat
    path("api/ai/", include("ai.urls")),                 # AI
    path("api/analytics/", include("analytics.urls")),   # Analytics
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
