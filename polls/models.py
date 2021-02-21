import datetime

from django.db import models
from django.utils import  timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200, help_text='问题的具体描述')
    pub_date = models.DateTimeField('date published', default=timezone.now, blank=True, help_text='问题发布日期')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, help_text='选择具体文字信息')
    votes = models.IntegerField(default=0, blank=True, help_text='该选择被投票次数')

    def __str__(self):
        return self.choice_text
