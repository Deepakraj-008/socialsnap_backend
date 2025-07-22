from django.db import models
from users.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    media = models.FileField(upload_to="posts/", blank=True, null=True)
    caption = models.TextField(blank=True)
    tags = models.JSONField(default=list)
    likes = models.ManyToManyField(User, related_name="liked_posts", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_story = models.BooleanField(default=False)
    expires_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Post by {self.user.username} - {self.created_at}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.id}"

