from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# post model 
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# comment model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# like model to track likes for a specific post
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user') 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')
