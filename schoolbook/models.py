from django.db import models
from django.utils.translation import gettext_lazy as _
from user.models import Grade


class SchoolBook(models.Model):
    title = models.CharField(_('title'), max_length=255)
    grade = models.ForeignKey(Grade, default=5, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(_('title'), max_length=255)
    url = models.URLField(unique=True)
    school_book = models.ForeignKey(SchoolBook, on_delete=models.CASCADE)

    def __str__(self):
        return self.title