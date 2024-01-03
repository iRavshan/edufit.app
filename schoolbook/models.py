from django.db import models
from django.utils.translation import gettext_lazy as _
from user.models import Grade
from competition.models import Subject
from ckeditor.fields import RichTextField


class SchoolBook(models.Model):
    subject = models.ForeignKey(Subject, null=False, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, default=5, on_delete=models.SET_DEFAULT)

    class Meta:
        ordering = ['subject']

    def __str__(self):
        return f'{self.grade.name} {self.subject.name}'


class Module(models.Model):
    title = models.CharField(_('title'), max_length=255, null=False)
    school_books = models.ManyToManyField(SchoolBook)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(_('title'), max_length=255, null=False)
    video_url = models.URLField(null=True)
    content = RichTextField(_('content'), null=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return self.title