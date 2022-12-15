from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class News1(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}: {self.content[:20]}'