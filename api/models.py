from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    file_name = models.CharField(max_length=255, default='')
    file_content = models.BinaryField(blank=True, null=True)
    mime_type = models.CharField(max_length=100, blank=True, null=True)


class Article(models.Model):
    title=models.CharField(max_length=300)
    content=models.TextField(default='')
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    uploaded_file = models.ForeignKey(File, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title
