from uuid import uuid4
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from user.models import Grade
from competition.models import Subject
from ckeditor.fields import RichTextField


class SchoolBook(models.Model):
    subject = models.ForeignKey(Subject, null=False, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, default=5, on_delete=models.SET_DEFAULT)
    slug = models.SlugField(unique=True, max_length=200, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.subject.name + self.grade.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['subject']

    def __str__(self):
        return f'{self.grade.name} {self.subject.name}'


class Module(models.Model):
    title = models.CharField(_('title'), max_length=255, null=False)
    school_books = models.ManyToManyField(SchoolBook)
    slug = models.SlugField(unique=True, max_length=300, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid4, editable=False, auto_created=True)
    title = models.CharField(_('title'), max_length=255, null=False)
    video_url = models.URLField(null=True)
    content = RichTextField(_('content'), null=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=300, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title