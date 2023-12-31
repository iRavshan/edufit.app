import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

class JobCategory(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, null=False, default=uuid.uuid4)
    name = models.CharField(_('name'), null=False, max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class JobSubcategory(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, null=False, default=uuid.uuid4)
    name = models.CharField(_('name'), null=False, max_length=50, unique=True)
    category = models.ForeignKey(JobCategory, null=False, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name
        