from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    createat = models.DateTimeField(auto_now=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username
