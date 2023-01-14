from django.db import models
from django.conf import settings

class Recipe(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    created_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title