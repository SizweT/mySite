# polls/models.py
from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # Foreign key relationship with the Question model
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    # Choice options: Yes or No
    CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    # Choice field to represent the voting options
    choice_text = models.CharField(max_length=3, choices=CHOICES)

    # Votes count for the choice
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
