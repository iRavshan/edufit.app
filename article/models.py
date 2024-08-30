from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from user.models import CustomUser
from schoolbook.models import Subject
from common.models import BaseModel


class Article(BaseModel):
    title = models.CharField(_('title'), max_length=100, null=False)
    content = RichTextField(_('content'), null=False)
    author = models.ForeignKey(CustomUser, null=False, blank=True, on_delete=models.CASCADE, related_name='articles')
    subjects = models.ManyToManyField(Subject)
    slug = models.SlugField(unique=True, max_length=300, blank=True, editable=False)
    viewers = models.ManyToManyField(CustomUser, blank=True)

    class Meta:
        unique_together = ('author', 'slug')
        ordering = ['-created']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title