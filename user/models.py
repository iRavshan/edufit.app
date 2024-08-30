import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager 


class Grade(models.Model):
    name = models.CharField(_('name'), max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(_('name'), max_length=200, unique=True)
    slug = models.SlugField(unique=True, max_length=300, blank=True, editable=False)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, auto_created=True)
    phone_number = models.CharField(null=False, max_length=13, unique=True)
    grade = models.ForeignKey(Grade, null=True, blank=True, on_delete=models.SET_NULL)
    institution = models.ForeignKey(Institution, null=True, blank=True, on_delete=models.SET_NULL)

    username = None
    email = None

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []    

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number