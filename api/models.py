from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title=models.CharField(max_length=300)
    content=models.TextField(default='')
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    file=models.FileField(upload_to='article_files/', blank=True, null=True)
            
    def __str__(self):
        return self.title
