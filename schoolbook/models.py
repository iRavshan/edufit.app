from uuid import uuid4
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from user.models import Grade, CustomUser
from ckeditor.fields import RichTextField


class Subject(models.Model):
    name = models.CharField(_('name'), max_length=50, null=False, unique=True)
    slug = models.SlugField(unique=True, max_length=300, blank=True, editable=False)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class SchoolBook(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid4, editable=False, auto_created=True)
    subject = models.ForeignKey(Subject, null=False, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, default=5, on_delete=models.SET_DEFAULT)
    slug = models.SlugField(unique=True, max_length=200, blank=True, editable=False)

    class Meta:
        ordering = ['subject']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.grade.name + '-' + self.subject.slug)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.grade.name} {self.subject.name}'


class Module(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid4, editable=False, auto_created=True)
    title = models.CharField(_('title'), max_length=255, null=False)
    school_books = models.ManyToManyField(SchoolBook)
    slug = models.SlugField(unique=True, max_length=300, blank=True, editable=False)
    instructors = models.ManyToManyField(CustomUser, blank=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid4, editable=False, auto_created=True)
    title = models.CharField(_('title'), max_length=255, null=False)
    video_url = models.URLField(null=True, blank=True)
    content = RichTextField(_('content'), null=True, blank=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=300, blank=True)

    class Meta:
        ordering = ['name']
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title