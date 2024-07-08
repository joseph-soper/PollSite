import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    ''' Question '''
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        ''' return string '''
        return self.question_text

    def was_published_recently(self):
        ''' was Question published within the last 24 hours? '''
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    ''' Question '''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        ''' return string '''
        return self.choice_text
