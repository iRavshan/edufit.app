from uuid import uuid4
from datetime import datetime
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from user.models import Grade, CustomUser
from schoolbook.models import Subject
from ckeditor.fields import RichTextField


class Question(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid4, editable=False, auto_created=True)
    
    TEXT = 'TEXT'
    SINGLE_CHOICE = 'SINGLE_CHOICE'
    MULTIPLE_CHOICE = 'MULTIPLE_CHOICE'

    QUESTION_TYPES = [
        (TEXT, 'Text Answer'),
        (SINGLE_CHOICE, 'Single Choice'),
        (MULTIPLE_CHOICE, 'Multiple Choice'),
    ]

    text = RichTextField(null=False)
    type = models.CharField(max_length=15, choices=QUESTION_TYPES)

    class Meta:
        ordering = ['type', 'text']
    
    def __str__(self):
        return self.text
    

class Choice(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid4, editable=False, auto_created=True)
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)
    text = RichTextField(_('text'), null=False, max_length=300)
    is_correct = models.BooleanField(default=False, null=False)
    
    class Meta:
        ordering = ['question']

    def __str__(self):
        return self.text


class Test(models.Model):
    allowed_subject = models.ForeignKey(Subject)    
    allowed_grade = models.ForeignKey(Grade)
    questions = models.ManyToManyField(Question, related_name='tests')
    shuffle_questions = models.BooleanField(_('Savollarni aralashtirish?'), default=False, null=False)
    shuffle_options = models.BooleanField(_('Variantlarni aralashtirish?'), default=False, null=False)
    
    def __str__(self):
        return f'{self.allowed_grade} {self.allowed_subject}'
    


class Competition(models.Model):
    name = models.CharField(_('name'), max_length=100, null=False, unique=True)
    subtitle = models.CharField(_('subtitle'), max_length=200, null=True)
    description = RichTextField(_('description'), null=True, blank=True)
    tests = models.ManyToManyField(Test, related_name='competitions')
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    slug = models.SlugField(unique=True, max_length=300, blank=True, editable=False)

    class Meta:
        ordering = ['-start_at']
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    


class QuestionAttempt(models.Model):
    user_attempt = models.ForeignKey('UserAttempt', on_delete=models.CASCADE, related_name='question_attempts')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_attempts')
    selected_choices = models.ManyToManyField(Choice, blank=True)
    text_answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user_attempt.user} - {self.question.id} - {self.user_attempt.competition.name}'   


class UserAttempt(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid4, editable=False, auto_created=True)
    user = models.ForeignKey(CustomUser, null=False, on_delete=models.CASCADE, related_name='attempts')
    competition = models.ForeignKey(Competition, null=False, on_delete=models.CASCADE, related_name='attempts')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='attempts')
    started_at = models.DateTimeField(default=datetime.now, null=False)
    finished = models.BooleanField(default=False, null=False)
    finished_at = models.DateTimeField(null=True)
    
    class Meta:
        ordering = ['-finished_at']

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}: {self.test}'