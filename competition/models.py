from uuid import uuid4
from datetime import datetime
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from user.models import Grade, CustomUser
from schoolbook.models import Subject
from ckeditor.fields import RichTextField


class Competition(models.Model):
    title = models.CharField(_('title'), max_length=100, null=False, unique=True)
    subtitle = models.CharField(_('subtitle'), max_length=200, null=True)
    description = RichTextField(_('description'), null=True)
    subjects = models.ManyToManyField(Subject)
    grades = models.ManyToManyField(Grade)
    start_at = models.DateTimeField(null=True)
    terminated = models.BooleanField(default=False, null=False)
    slug = models.SlugField(unique=True, max_length=300, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-start_at']

    def __str__(self):
        return self.title


class Question(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid4, editable=False, auto_created=True)
    text = RichTextField(_('text'), null=False)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Option(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid4, editable=False, auto_created=True)
    text = RichTextField(_('text'), null=False)
    is_correct = models.BooleanField(default=False, null=False)
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text


class Attempt(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid4, editable=False, auto_created=True)
    user = models.ForeignKey(CustomUser, null=False, on_delete=models.CASCADE)
    options = models.ManyToManyField(Option)
    started_at = models.DateTimeField(default=datetime.now, null=False)
    finished = models.BooleanField(default=False, null=False)
    finished_at = models.DateTimeField(null=True)
    score = models.PositiveIntegerField(null=True)
    competition = models.ForeignKey(Competition, null=False, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ['-finished_at']

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}: {self.score}'