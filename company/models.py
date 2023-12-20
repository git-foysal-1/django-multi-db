from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    employees = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name