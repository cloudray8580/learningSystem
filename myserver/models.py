from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.TextField(max_length=20000)
