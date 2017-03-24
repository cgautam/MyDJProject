from __future__ import unicode_literals


import datetime


from django.db import models
from django.utils import timezone


class Ques(models.Model):
    ques_text = models.CharField(max_length=200)
    q_date = models.DateTimeField('date assigned')


    def __unicode__(self):
        return self.ques_text

    def published_now(self):
        return self.q_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
	ques = models.ForeignKey(Ques)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)


	def __unicode__(self):
		return self.choice_text
