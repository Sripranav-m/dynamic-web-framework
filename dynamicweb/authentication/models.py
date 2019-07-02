from django.db import models

# Create your models here.
from django.db import models

class userdata(models.Model):
    email=models.EmailField()
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    def __str__(self):
        return self.username
