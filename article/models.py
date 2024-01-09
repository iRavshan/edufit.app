from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from user.models import CustomUser
from schoolbook.models import Subject

class Article(models.Model):
    title = models.CharField(_('title'), max_length=100, null=False, unique=True)
    content = RichTextField(_('content'), null=False)
    author = models.ForeignKey(CustomUser, null=False, blank=True, on_delete=models.CASCADE, related_name='articles')
    created = models.DateTimeField(auto_now_add=True, auto_created=True)
    subjects = models.ManyToManyField(Subject)
    slug = models.SlugField(unique=True, max_length=300, blank=True)
    viewers = models.ManyToManyField(CustomUser, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title