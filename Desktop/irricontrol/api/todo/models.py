from django.db import models


class Todo (models.Model):
    titulo = models.CharField(max_length=100)
    descrição = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    altered_at = models.DateTimeField(auto_now=True)
