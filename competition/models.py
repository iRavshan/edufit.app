from django.db import models
from datetime import datetime
from uuid import uuid4
from user.models import Grade, CustomUser
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _


class Subject(models.Model):
    name = models.CharField(_('name'), max_length=50, null=False, unique=True)

    def __str__(self):
        return self.name


class Competition(models.Model):
    title = RichTextField(_('title'), max_length=100, null=False, unique=True)
    subtitle = models.CharField(_('subtitle'), max_length=200, null=True)
    description = RichTextField(_('description'), null=True)
    subjects = models.ManyToManyField(Subject)
    grades = models.ManyToManyField(Grade)
    start_at = models.DateTimeField(null=True)
    terminated = models.BooleanField(default=False, null=False)

    class Meta:
        ordering = ['start_at']

    def __str__(self):
        return self.title


class Question(models.Model):
    text = RichTextField(_('text'), null=False)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Option(models.Model):
    text = RichTextField(_('text'), null=False)
    is_correct = models.BooleanField(default=False, null=False)
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text


class Attempt(models.Model):
    user = models.ForeignKey(CustomUser, null=False, on_delete=models.CASCADE)
    options = models.ManyToManyField(Option)
    started_at = models.DateTimeField(default=datetime.now, null=False)
    finished = models.BooleanField(default=False, null=False)
    finished_at = models.DateTimeField(null=True)
    score = models.IntegerField(null=True)
    competition = models.ForeignKey(Competition, null=False, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
 
    class Meta:
        ordering = ['-finished_at']

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}: {self.score}'