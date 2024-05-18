from django.contrib import admin
from . import models

admin.site.register(models.Subject)
admin.site.register(models.Option)
admin.site.register(models.Question)
admin.site.register(models.Competition)
admin.site.register(models.Attempt)
admin.site.register(models.Answer)
