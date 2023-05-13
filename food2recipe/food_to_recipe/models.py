from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    food = models.CharField(max_length=50)
    createdDate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.food
    
    class Meta:
        ordering = ["createdDate"]