from django.db import models
from django.contrib.auth.models import User

class Programmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    language = models.CharField(max_length=255)
    framework = models.CharField(max_length=255)
    experience = models.IntegerField()

    def __str__(self):
        return self.user.username

class Project(models.Model):
    programmer = models.ForeignKey(Programmer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
