import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class JobSubcategory(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, null=False, default=uuid.uuid4)
    name = models.CharField(_('name'), max_length=50, unique=True)

    def __str__(self):
        return self.name
        

class JobCategory(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, null=False, default=uuid.uuid4)
    name = models.CharField(_('name'), max_length=50, unique=True)
    subcategories = models.ForeignKey(JobSubcategory, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name