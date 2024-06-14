
import email
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    messagge = models.TextField()
    
    def __str__(self):
        return self.name
    
class subscription(models.Model):
    email_subs= models.EmailField()
    
    def __str__(self):
        return self.email_subs