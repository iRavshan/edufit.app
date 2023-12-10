from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class Grade(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Institution(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    third_name = models.CharField(null=True, max_length=50)
    phone = models.CharField(null=False, max_length=20)
    grade = models.ForeignKey(Grade, null=True, on_delete=models.SET_NULL)
    institution = models.ForeignKey(Institution, null=True, on_delete=models.SET_NULL)


