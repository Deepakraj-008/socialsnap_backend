from django.urls import path
from .views import AnalyticEventListView

urlpatterns = [
    path("events/", AnalyticEventListView.as_view(), name="analytic-events"),
]

