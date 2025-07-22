# users/urls.py
from django.urls import path
from django.http import JsonResponse
from .views import RegisterView, LoginView, ProfileView

def users_root_view(request):
    return JsonResponse({
        "message": "Welcome to the Users API",
        "routes": [
            "/api/users/register/",
            "/api/users/login/",
            "/api/users/profile/"
        ]
    })

urlpatterns = [
    path("", users_root_view),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
