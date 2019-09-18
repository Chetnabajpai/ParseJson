from django.db import models
# Create your models here.


class Quiz(models.Model):
    topic = models.CharField(max_length=50)
    question = models.TextField(help_text='Type the question')

    def __str__(self):
        return self.topic


class Option(models.Model):
    question = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    option = models.CharField(max_length=50)

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    answer = models.CharField(max_length=30)

    def __str__(self):
        return self.question
