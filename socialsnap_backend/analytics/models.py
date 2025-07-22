from django.db import models
from users.models import User

class AnalyticEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    event_type = models.CharField(max_length=100)
    details = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_type} - {self.created_at}"

