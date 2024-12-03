from django.db import models
from django.contrib.auth.models import User  # Import the User model

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # New fields
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Author field, linked to the User model
    published_date = models.DateTimeField(null=True, blank=True)  # Published date, can be null

    def __str__(self):
        return self.title

