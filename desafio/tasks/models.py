from django.db import models

# Create your models here.

class Task(models.Model):
    empresa = models.CharField(max_length=255)
    ticker  = models.CharField(max_length=255)
    preco   = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.empresa
        
