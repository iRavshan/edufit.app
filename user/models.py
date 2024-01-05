import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Grade(models.Model):
    name = models.CharField(_('name'), max_length=50, unique=True)

    def __str__(self):
        return self.name

class Institution(models.Model):
    name = models.CharField(_('name'), max_length=200)
    slug = models.SlugField(unique=True, max_length=300, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    middle_name = models.CharField(null=True, max_length=50)
    phone = models.CharField(null=False, max_length=20, unique=True)
    grade = models.ForeignKey(Grade, null=True, on_delete=models.SET_NULL)
    institution = models.ForeignKey(Institution, null=True, on_delete=models.SET_NULL)


