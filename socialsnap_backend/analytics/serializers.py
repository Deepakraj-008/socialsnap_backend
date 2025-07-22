from rest_framework import serializers
from .models import AnalyticEvent

class AnalyticEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalyticEvent
        fields = "__all__"

