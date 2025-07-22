from rest_framework import generics, permissions
from .models import AnalyticEvent
from .serializers import AnalyticEventSerializer

class AnalyticEventListView(generics.ListAPIView):
    serializer_class = AnalyticEventSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admins can view

    def get_queryset(self):
        return AnalyticEvent.objects.all().order_by("-created_at")

