from __future__ import unicode_literals

from django.db import models

class Ques(models.Model):
    ques_text = models.CharField(max_length=200)
    q_date = models.DateTimeField('date assigned')


class Choice(models.Model):
	ques = models.ForeignKey(Ques)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
# Create your models here.
